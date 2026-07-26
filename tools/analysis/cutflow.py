"""
# cutflow.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.
"""
import json, os, math
from typing import Optional, List

from orchestral.tools.base.tool import BaseTool
from orchestral.tools.base.field_utils import RuntimeField, StateField


# Comparison operators allowed in a cut spec. Kept to a safe, explicit set so
# selections are declarative (no eval). Each maps a name to a 2-arg predicate.
_OPS = {
    ">":  lambda a, b: a > b,
    ">=": lambda a, b: a >= b,
    "<":  lambda a, b: a < b,
    "<=": lambda a, b: a <= b,
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
    "ge": lambda a, b: a >= b,
    "gt": lambda a, b: a > b,
    "le": lambda a, b: a <= b,
    "lt": lambda a, b: a < b,
    "eq": lambda a, b: a == b,
    "ne": lambda a, b: a != b,
}


def _obj_list(event_data: dict, obj_type: str) -> list:
    """Return the list of objects of a given type from an event's data block.

    Handles both reco-level collections (jets, electrons, muons, photons) and
    particle-level events (particles). `met` is special-cased: it is one dict
    per event, exposed as a one-element list so multiplicity/variable logic is
    uniform. An absent collection is an empty list (so '0 photons in any event'
    is naturally visible rather than a KeyError)."""
    if obj_type == "met":
        m = event_data.get("met")
        return [m] if isinstance(m, dict) else ([] if m is None else [{"met": m}])
    val = event_data.get(obj_type)
    if val is None:
        return []
    if isinstance(val, list):
        return val
    return [val]


def _get_var(obj: dict, variable: str) -> Optional[float]:
    """Pull a numeric variable from an object dict, deriving pt if needed."""
    if variable in obj:
        try:
            return float(obj[variable])
        except (TypeError, ValueError):
            return None
    # Derive pT from a 4-vector if a 'pt'/'pT' key is absent.
    if variable in ("pt", "pT") and "px" in obj and "py" in obj:
        try:
            return math.sqrt(float(obj["px"]) ** 2 + float(obj["py"]) ** 2)
        except (TypeError, ValueError):
            return None
    # Allow capitalization variants (pt/PT, eta/Eta, ...).
    for k in obj:
        if k.lower() == variable.lower():
            try:
                return float(obj[k])
            except (TypeError, ValueError):
                return None
    return None


def _event_passes_cut(event_data: dict, cut: dict) -> bool:
    """Evaluate one structured cut against an event.

    A cut is a dict: {name, object, variable, op, threshold, [count_min]}.
      - object: collection name (e.g. 'photon'/'photons', 'jet'/'jets', 'met').
      - variable: per-object numeric field (e.g. 'pt', 'eta'); optional.
      - op/threshold: comparison applied per object; an object passes if true.
      - count_min (default 1 when variable/op given, else from threshold): the
        event passes if at least `count_min` objects pass. With no variable, the
        cut is a pure multiplicity requirement: count(objects) op threshold.
    """
    obj_type = cut.get("object")
    # Normalize singular -> plural for reco collections.
    aliases = {
        "photon": "photons", "jet": "jets", "electron": "electrons",
        "muon": "muons", "particle": "particles",
    }
    obj_type = aliases.get(obj_type, obj_type)
    objs = _obj_list(event_data, obj_type)

    op_name = cut.get("op")
    threshold = cut.get("threshold")
    variable = cut.get("variable")

    if op_name is not None and op_name not in _OPS:
        raise ValueError(f"unknown op '{op_name}'; allowed: {sorted(_OPS)}")

    # Pure multiplicity cut: no per-object variable -> compare the count.
    if variable is None:
        op = _OPS[op_name] if op_name is not None else _OPS[">="]
        return bool(op(len(objs), threshold))

    # Per-object variable cut: count objects passing variable op threshold.
    op = _OPS[op_name] if op_name is not None else _OPS[">="]
    n_pass = 0
    for o in objs:
        v = _get_var(o, variable)
        if v is None:
            continue
        if op(v, threshold):
            n_pass += 1
    count_min = cut.get("count_min", 1)
    return n_pass >= count_min


class CutflowTool(BaseTool):
    """
    Read-only selection-sanity / cutflow diagnostic for a JSONL event dataset.

    This is a DIAGNOSTIC, not a histogram filler. It directly closes the silent
    "passed events = 0" failure: it streams the events and reports
      (i)   total events,
      (ii)  per-object mean/max multiplicity (so '0 photons in any event' is
            immediately visible),
      (iii) a CUTFLOW — events surviving after each cut, applied in order,
      (iv)  `zeroed_by`: the name of the first cut that drops the surviving
            count to 0 (or null if no cut zeros the sample).

    Inputs (runtime):
      - events_path: sandbox-relative JSONL of reco/particle events
        (schema {"data": {<collection>: [...] | met:{...}}}).
      - cuts: ordered list of structured cut specs. Each is a dict:
          {name, object, variable, op, threshold, [count_min]}
        e.g. {"name":">=1 photon pt>40","object":"photons","variable":"pt",
              "op":">","threshold":40.0,"count_min":1}
        or a pure multiplicity cut {"name":"njet>=2","object":"jets",
              "op":">=","threshold":2}.
        Allowed ops: > >= < <= == != (and word aliases gt/ge/lt/le/eq/ne).
      - object_counts: optional list of object types to report multiplicity for
        (e.g. ["photons","jets","met"]).

    Output (JSON): total_events, multiplicity stats, cutflow list, zeroed_by.
    """
    # --------------------------- Runtime fields --------------------------- #
    events_path: str = RuntimeField(description="Sandbox-relative path to a JSONL event dataset")
    cuts: Optional[List[dict]] = RuntimeField(
        default=None,
        description="Ordered list of structured cut specs {name,object,variable,op,threshold,[count_min]}. Pure multiplicity cuts omit 'variable'."
    )
    object_counts: Optional[List[str]] = RuntimeField(
        default=None,
        description="Object types to report mean/max multiplicity for, e.g. ['photons','jets','met']"
    )
    # ---------------------------------------------------------------------- #

    # ---------------------------- State fields ---------------------------- #
    base_directory: str = StateField(default=".", description="Base directory for safe paths")
    # ---------------------------------------------------------------------- #

    def _setup(self):
        self.base_directory = os.path.abspath(self.base_directory)
        if not os.path.exists(self.base_directory):
            raise ValueError(f"Base directory does not exist: {self.base_directory}")

    def _safe_path(self, rel: str) -> Optional[str]:
        if not rel:
            return None
        full = os.path.abspath(os.path.join(self.base_directory, rel))
        return full if full.startswith(self.base_directory) else None

    @staticmethod
    def compute(events: List[dict], cuts: Optional[List[dict]],
                object_counts: Optional[List[str]]) -> dict:
        """Pure computation over a list of parsed events. Returns the result
        dict. Separated so it is unit-testable without file I/O."""
        n_events = len(events)
        data_blocks = [ev.get("data", ev) if isinstance(ev, dict) else {} for ev in events]

        # (ii) per-object multiplicity stats.
        aliases = {
            "photon": "photons", "jet": "jets", "electron": "electrons",
            "muon": "muons", "particle": "particles",
        }
        wanted = object_counts
        if not wanted:
            # Auto-discover collection names present across events.
            keys = set()
            for d in data_blocks:
                if isinstance(d, dict):
                    keys.update(d.keys())
            wanted = sorted(keys)
        multiplicity = {}
        for ot in wanted:
            ot_norm = aliases.get(ot, ot)
            counts = [len(_obj_list(d, ot_norm)) for d in data_blocks]
            if counts:
                multiplicity[ot] = {
                    "mean": sum(counts) / len(counts),
                    "max": max(counts),
                    "min": min(counts),
                }
            else:
                multiplicity[ot] = {"mean": 0.0, "max": 0, "min": 0}

        # (iii)+(iv) cutflow.
        cutflow = [{"cut": "initial", "passed": n_events}]
        zeroed_by = None
        surviving = list(range(n_events))  # indices of currently-surviving events
        for cut in (cuts or []):
            name = cut.get("name", f"cut{len(cutflow)}")
            kept = [i for i in surviving if _event_passes_cut(data_blocks[i], cut)]
            cutflow.append({"cut": name, "passed": len(kept)})
            if len(kept) == 0 and zeroed_by is None and len(surviving) > 0:
                zeroed_by = name
            surviving = kept

        return {
            "status": "ok",
            "total_events": n_events,
            "multiplicity": multiplicity,
            "cutflow": cutflow,
            "final_passed": (cutflow[-1]["passed"] if cutflow else n_events),
            "zeroed_by": zeroed_by,
        }

    def _run(self) -> str:
        src = self._safe_path(self.events_path)
        if not src:
            return self.format_error(error="Access Denied", reason="events_path escapes base_directory")
        if not os.path.exists(src):
            return self.format_error(error="File Not Found", reason=f"Events file not found: {self.events_path}")

        try:
            events = []
            with open(src, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        events.append(json.loads(line))
        except Exception as e:
            return self.format_error(error="Read Error", reason=str(e))

        if not events:
            return self.format_error(
                error="Empty Input",
                reason=f"No events found in {self.events_path}",
                suggestion="Check that the upstream stage produced events; a 0-event file usually means the generation/conversion step failed."
            )

        # Validate cut specs (op names) up front for a clean error.
        for cut in (self.cuts or []):
            if not isinstance(cut, dict):
                return self.format_error(
                    error="Invalid Cut",
                    reason="each cut must be a dict {name,object,variable,op,threshold}",
                )
            if cut.get("op") is not None and cut["op"] not in _OPS:
                return self.format_error(
                    error="Invalid Cut",
                    reason=f"unknown op '{cut['op']}' in cut '{cut.get('name')}'",
                    suggestion=f"allowed ops: {sorted(_OPS)}"
                )

        try:
            result = self.compute(events, self.cuts, self.object_counts)
        except Exception as e:
            return self.format_error(error="Processing Error", reason=str(e))

        return json.dumps(result, separators=(",", ":"), ensure_ascii=False)
