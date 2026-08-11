# Error decoder

When the heptapod `MadGraphFromRunCard` tool returns `Could not locate unweighted_events.lhe`, **read `runs/.../mg5_run.log`**, then `runs/.../MG5_debug` for the full traceback. Cross-reference here.

## "name MX define multiple time. Please correct the UFO model!"
- **Real cause:** Mass or width parameter declared in both `M$Parameters` and the particle class `Mass -> {MX, val}`.
- **Fix:** See pitfall **P1**. Remove from `M$Parameters`.

## "Some couplings have '1' order. This is not allowed in MG."
- **Real cause:** BSM coupling has no `InteractionOrder` tag; FR fell back to `{'1':1}`.
- **Fix:** See pitfall **P2**. Add `M$InteractionOrderHierarchy` and tag each BSM parameter with `InteractionOrder -> {NP, 1}`.

## "UFOError : invalid syntax (object_library.py, line 268)"
- **Real cause:** MG5 auto-conversion mask. The actual problem is one of P1 or P2; the converter exits with a generic SyntaxError that points at object_library.py.
- **Fix:** Run mg5_aMC directly with `import model /path` from the shell. The first attempt fails, MG5 calls auto-convert, the second attempt then surfaces the real error.

## "fail to load model but auto_convert_model is on True. Trying to convert the model"
- **Real cause:** Your UFO is in old-style FR 2.3 format and MG5 3.6+ wants UFO 2.0 (Python 3-style imports).
- **Status:** Informational, not fatal *by itself*. MG5 auto-converts in place. If subsequent error is "invalid syntax", see above. If it loads, you're fine.
- **Optional cleanup:** add `from __future__ import absolute_import` to UFO `__init__.py` and convert relative imports — but auto-convert handles it for normal usage.

## "Process has 1 diagrams" repeated, then "0 processes generated"
- **Real cause:** Your `generate` syntax referenced a particle name that isn't recognized.
- **Fix:** Check `particles.py` for the exact `name` field — that's what MG5 wants. PDG-id is fine too via `pdg_id->...`. For self-conjugate particles, you can't use `~` suffix.

## "No diagrams for ta- > mu- mu+ mu- mu+ mu-" with `NP=N`
- **Real cause:** Your interaction-order constraint excludes the topology you wanted. Recount BSM vertices on the cascade diagram.
- **Debug:** Run without the order constraint first to see all diagrams, then constrain.

## "MadGraph error: Particle 9000022 not found" when running `output`
- **Real cause:** PDG ID collision with another model already loaded, or the UFO was not actually re-imported after edit.
- **Fix:** Restart MG5 between models; or use `import model -modelname=fresh /path`.

## Empty LHE / "0 events"
- **Real cause:** Cross-section integration converged to numerically-zero value because:
  - Couplings are too small (e.g. `eps = 1e-10`),
  - Or the wrong process / no s-channel resonance available,
  - Or kinematic cuts in `run_card.dat` exclude all phase space.
- **Fix:** Check `cross_section_<run>.txt` in the run folder. If $\sigma$ is tiny, increase couplings or remove cuts; if exactly zero, fix the process.

## "InvalidCmd : No processes generated. Please generate a process first."
- **Real cause:** `compute_widths` was placed AFTER `output` (or `launch`) in the MG5 card. `compute_widths` reloads the model and clears MG5's process/output state, so the next `launch` finds nothing.
- **Tell:** Log shows successful `generate ... @1` with N diagrams, successful `output ...`, then `compute_widths` runs ("Results written to .../param_card.dat"), then `launch` errors as above with `output command missing, run it automatically (with default argument)`.
- **Fix:** See pitfall **P12**. Move `compute_widths phid Ap` to BEFORE `generate` (immediately after `import model`). Widths land in `UFO/param_card.dat` and `output` copies them into the process `Cards/`.

## "InvalidCmd: phid is not a valid name"
- **Real cause:** `import model` failed silently *before* this command, so the BSM particle isn't in MG5's name space.
- **Fix:** Read upstream log; the `import` itself errored. Fix that and re-run.

## Common Mathematica/FeynRules errors

### "FeynRulesPath must be a directory. Got: /path/to/FeynRules_v..."
- **Cause:** The MCP server's `FR_PATH` env is unset or set to a placeholder.
- **Fix:** Either configure MCP server env, or run wolframscript directly. See pitfall **P9**.

### "LoadModel::nofile" / "Cannot open SM.fr"
- **Cause:** Working directory or `$FeynRulesPath` not set before `LoadModel`.
- **Fix:** Wrap the script with `SetDirectory[$FeynRulesPath]; LoadModel["Models/SM/SM.fr", "your_model.fr"]`.

### "WriteUFO::lengthMismatch"
- **Cause:** Lagrangian contains a free Lorentz or color index that's not contracted, or a particle reference with the wrong number of indices.
- **Fix:** Audit each new Lagrangian term; check that every `Ga[mu]` is paired with another `[mu]`, every `del[X, mu]` matches.

### "CheckHermiticity::nonHermitian"
- **Cause:** A Lagrangian term lacks its Hermitian conjugate, or has a relative phase.
- **Fix:** For LFV-like operators: `LLFV := -y phi (psibar.ProjP.chi + chibar.ProjM.psi)` (both terms required).

## Numerical / runtime issues

### Reconstructed peak much wider than expected (factor 10–100×)
- **Likely:** Width placeholder is hitting MG5's numerical floor (~1e-3 × M). See pitfall **P4**.
- **Fix:** Use `compute_widths` or set width explicitly to ≤ 1e-15 GeV (true delta) or ≥ realistic value.

### Energy non-conservation in LHE
- **Cause:** Almost always a model bug (wrong vertex, missing kinetic term, gauge non-invariance), not MG5's fault.
- **Diagnose:** For a single event, sum status=1 4-momenta and compare to incoming. >1e-6 GeV mismatch is real.

### Spin correlations look wrong
- **Cause:** Used MadSpin where you wanted explicit ME, or vice versa. MadSpin loses some correlations across the production-decay split.
- **Fix:** For correlation-critical analyses, use the explicit n-body ME (pitfall **P3**, P10).
