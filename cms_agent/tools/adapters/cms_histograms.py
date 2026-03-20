"""Histogram adapter for CMS nano-like tables.

This stays intentionally light-weight: it accepts plain Python / NumPy-friendly
column mappings so the contract can be exercised outside a full CMSSW or coffea
environment.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import numpy as np


def _to_1d_array(values: Any) -> np.ndarray:
    arr = np.asarray(values, dtype=np.float64)
    if arr.ndim == 0:
        arr = arr.reshape(1)
    return arr.reshape(-1)


def _json_ready(values: np.ndarray) -> list[float]:
    return [float(v) for v in values.tolist()]


def build_leading_pt_histogram(
    table: Mapping[str, Any],
    field_pt: str = "Photon_pt",
    bins: int = 24,
    value_range: tuple[float, float] = (0.0, 240.0),
    png_path: str | None = None,
) -> dict[str, Any]:
    """
    Build a JSON-serializable leading-pT histogram.

    Parameters
    ----------
    table :
        Mapping of column name -> array-like values.
    field_pt :
        Column storing photon transverse momentum in GeV.
    bins :
        Number of equally spaced histogram bins.
    value_range :
        Inclusive lower edge and upper edge used for histogramming.
    png_path :
        Optional output path placeholder for downstream renderers. This function
        does not draw plots; it only records the intended artifact location.

    Returns
    -------
    dict
        JSON-serializable histogram representation + optional PNG path.
    """
    if field_pt not in table:
        raise KeyError(f"Missing required field: {field_pt}")

    values = _to_1d_array(table[field_pt])
    if values.size == 0:
        raise ValueError(f"Field {field_pt} is empty")

    finite_mask = np.isfinite(values)
    if not np.all(finite_mask):
        values = values[finite_mask]
    if values.size == 0:
        raise ValueError(f"Field {field_pt} contains no finite values")

    hist, edges = np.histogram(values, bins=bins, range=value_range)
    result = {
        "field": field_pt,
        "entries": int(values.size),
        "bin_edges": _json_ready(edges),
        "counts": [int(v) for v in hist.tolist()],
        "underflow": int(np.sum(values < value_range[0])),
        "overflow": int(np.sum(values > value_range[1])),
        "summary": {
            "mean": float(values.mean()),
            "std": float(values.std()),
            "min": float(values.min()),
            "max": float(values.max()),
        },
    }
    if png_path:
        result["png_path"] = str(Path(png_path))
    return result
