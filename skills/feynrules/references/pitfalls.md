# Pitfalls catalog (feynrules)

Pitfalls that bite while writing the `.fr` and compiling the UFO.
For failures that appear once MG5 is running, see the `mg5` skill.

## P1. Duplicate mass/width parameter

**Symptom (MG5):** `name MX define multiple time. Please correct the UFO model!`

**Cause:** Particle class `Mass -> {MX, val}` auto-declares `MX`. Adding another entry in `M$Parameters` with the same name produces a duplicate.

**Fix:** Remove from `M$Parameters`. Only add to `M$Parameters` with `ParameterType -> Internal` if the mass is a derived quantity (e.g., `MZprime = gx * vx`).

## P2. Coupling with no interaction order

**Symptom (MG5):** `Some couplings have '1' order. This is not allowed in MG.`

**Cause:** A coupling expression contains only BSM parameters (no `ee`, `gs`, SM Yukawas) and FeynRules has no order to assign. Falls back to a placeholder `{'1':1}`.

**Fix:** Two changes in the `.fr`:

1. Declare an `NP` order block:
   ```mathematica
   M$InteractionOrderHierarchy = {{QCD,1},{QED,2},{NP,1}};
   M$InteractionOrderLimit     = {{QCD,99},{QED,99},{NP,99}};
   ```

2. Tag every BSM external parameter:
   ```mathematica
   gNew == { ParameterType -> External, ..., InteractionOrder -> {NP, 1} }
   ```

Mixed BSM×SM couplings (like `eps * ee`) inherit the right combined order automatically.

**Verification:** After regenerating UFO, `grep "'1':1" UFO/couplings.py` must return nothing.

## P5. Lorentz index `mu` collides with muon name

**Symptom:** Compilation OK but Feynman rules contain wrong propagator structures, or runtime errors deep in FeynRules.

**Cause:** FR's `Ga[mu]`, `del[psi, mu]`, and `FS[A, mu, nu]` all use `mu` as a Lorentz index symbol. The SM particle class also defines `mu` as the muon field. FR resolves by context, but you can construct ambiguous expressions.

**Defensive pattern:** Use distinct Lorentz index letters in BSM Lagrangian terms, e.g.
```mathematica
LphiAA := gphiAA phid Aprime[lor1] Aprime[lor1];
LFmunu := -1/4 FS[Aprime, lor1, lor2] FS[Aprime, lor1, lor2];
```
or just rebind the Lorentz indices inside `Block[{...}, ...]`.

## P6. Self-conjugate vector — Stuckelberg vs broken U(1)'

**Symptom:** Hidden U(1)' models compiled without the dark Higgs scalar give massless dark photon (or weird unitarity violations at high energy in cross sections).

**Cause:** A massive vector field needs a Higgs (or Stückelberg field) for its longitudinal mode. FR `Mass -> {MA, val}` simply gives the vector a Proca mass term, which is fine for tree-level cross sections but unphysical at high energies. Also the goldstone doesn't appear automatically.

**Practical guidance:** For LHC-scale processes with $\sqrt{s} \gg M_{A'}$, the longitudinal mode must be present. For low-energy ($\tau$ decays, $B$-meson decays) the Proca mass is fine. If in doubt, write the dark Higgs explicitly.

## P7. ChiralProjector convention

**Symptom:** Wrong sign on chiral coefficient or coupling appears as $g_L$ when you wanted $g_R$.

**Reference:**
- `ProjM = (1 - γ⁵)/2 = P_L`
- `ProjP = (1 + γ⁵)/2 = P_R`

For a scalar bilinear $\bar\psi_L \chi_R = \bar\psi\,P_R\,\chi$ → `psibar.ProjP.chi`.
For a current $\bar\psi_L\,\gamma^\mu\,\chi_L = \bar\psi\,\gamma^\mu\,P_L\,\chi$ → `psibar.Ga[mu].ProjM.chi`.

## P9. FR_PATH not propagating to MCP server

**Symptom:** Heptapod `FeynRulesToUFO` errors with `FeynRulesPath must be a directory. Got: /path/to/FeynRules_v2.X.X` despite the env var being set in your shell.

**Cause:** The MCP server runs in its own process and doesn't inherit shell env vars set after server startup.

**Fix:** Set `FR_PATH` in MCP server's launch environment (e.g., in `~/.claude/mcp.json` or a wrapper script). Alternatively, fall back to running wolframscript directly with absolute paths.
