# Pitfalls catalog (mg5)

Pitfalls that bite while generating events from a UFO.
For failures in the model itself, see the `feynrules` skill.

## P3. Decay-chain comma syntax does not unfold ≥3 levels reliably

**Symptom:** `generate ta- > mu- phid, phid > Ap Ap, Ap > mu+ mu-` produces 5-particle LHE events with `Ap` status=1 (not decayed) instead of 9-particle events with full cascade.

**Cause:** MG5 generates each comma-separated subprocess but does not always weave the third level into the final-state record, especially when the second level introduces multiple identical particles.

**Fix (preferred):** Write the explicit n-body matrix element with an interaction-order constraint that picks out only the target topology:

```
generate ta- > mu- mu- mu- mu+ mu+ NP=4
```

The `NP=4` excludes any contribution that doesn't go through the 4-vertex cascade.

**Fix (alt):** Use parenthesized grouping per distinct decay:

```
generate ta- > mu- phid, (phid > Ap Ap, Ap > mu+ mu-)
```

Even with parens, verify by inspecting the first event's particle count.

**Always verify:** After `launch`, look at `head -1 events.jsonl | python -c "import json,sys; print(len(json.loads(sys.stdin.read())['data']['particles']))"` — count must equal incoming + intermediates + finals.

## P4. Widths left at placeholder cause numerical artifacts

**Symptom:** Reconstructed peak has a finite spread larger than the analytic Breit–Wigner FWHM (often ~$10^{-3}$ × $M$).

**Cause:** MG5 has internal numerical floors near very small widths. A placeholder `Wphid = 1e-9 GeV` is not actually used as the BW width near the pole.

**Fix:**

- **Realistic widths:** add `compute_widths phid Ap` BEFORE `generate` in the MG5 card. It writes to the UFO's `param_card.dat`; the subsequent `output` then copies that into the process `Cards/`. Doing it after `output` or `launch` instead is the bug in **P12**.
- **True narrow-width:** set widths to `1e-15` (smaller than MG5's floor), accept that the peak is delta-function-like.
- **Observation:** for parton-level peaks, the dominant broadening in real experiments is detector resolution + ISR/FSR, both injected post-LHE via Pythia/Delphes, not changes to the param card.

## P8. Confusing MG5 auto-conversion error masks real one

**Symptom:** `UFOError: invalid syntax (object_library.py, line 268)` — does not point at any actual syntax problem.

**Cause:** MG5 attempts to auto-convert old-style (Python 2) UFOs and that conversion path raises a generic syntax error that masks the underlying issue (typically pitfalls P1 or P2).

**Fix:** Run MG5 directly on a minimal command file to surface the real error:
```bash
echo "import model /full/path/to/UFO_dir" > /tmp/_t.txt
$MG5_PATH/bin/mg5_aMC -f /tmp/_t.txt 2>&1 | tail -30
```
The next-actual-error message ("name MX define multiple time" or "Some couplings have '1' order") tells you which pitfall fired.

## P10. MadSpin vs decay-chain vs explicit ME — which to choose

| Approach | When to use | Cost | LHE quality |
|---|---|---|---|
| Comma decay chain `, X > Y Z` | 1–2 level cascades, narrow widths | Free | Good for shallow chains |
| Parenthesized chain | Distinct decaying particles | Free | Good |
| Explicit n-body ME with `NP=N` | Deep cascades, want exact correlations | Slower (n! diagrams) | Best |
| MadSpin | Decoupling production from decay; want easy reweighting | Adds post-processing step | Loses some spin correlations |

For our $\tau\to 5\mu$ via 3-level cascade, the explicit ME with `NP=4` gave the cleanest result. For $H\to ZZ\to 4\ell$, the parenthesized chain is fine.

## P11. Verify the LHE before histogramming 5000 events

A 5-second sanity check that catches almost everything:

```python
import json
e = json.loads(open('events.jsonl').readline())
parts = e['data']['particles']
print(len(parts), [(p['id'], p.get('status')) for p in parts])
# Expect for tau- > 5mu cascade:
# 9 [(15,-1), (13,1), (9000006,2), (9000022,2), (9000022,2), (13,1), (-13,1), (13,1), (-13,1)]
```

If status flags are wrong or particle count is short, fix the MG5 card before generating bulk.

## P12. `compute_widths` after `output`/`launch` discards the generated process

**Symptom:** MG5 logs show successful `generate` (with N diagrams) and successful `output`, then `compute_widths phid Ap` runs and writes a new `param_card.dat`, then `launch` errors with:

```
output command missing, run it automatically (with default argument)
InvalidCmd : No processes generated. Please generate a process first.
```

The heptapod tool reports `Could not locate unweighted_events.lhe`.

**Cause:** `compute_widths` triggers `model.find_vertexlist()` and reloads the model, which clears MG5's process and output state. The subsequent `launch` then has no process to launch and tries to re-`output`, but with nothing to output.

**Fix:** Put `compute_widths` BEFORE `generate`, so the widths land in the UFO's `param_card.dat` and `output` propagates that file into the process `Cards/`:

```
import model UFO_dir
compute_widths phid Ap     # writes UFO_dir/param_card.dat
generate ta- > mu- mu- mu- mu+ mu+ NP=4
output proc_dir            # copies UFO_dir/param_card.dat into proc_dir/Cards/
launch
set nevents 1000
...
```

**Why this works:** `compute_widths` only needs the model loaded (which `import model` already did); it does not need any process. The 2-body widths are computed from the FeynRules formula, not from generated processes ("INFO: Get two body decay from FeynRules formula"). The 3+ body fallback is also not process-dependent. So computing widths before `generate` is fully equivalent in width quality, and avoids the state-reset bug.

**Verification:** After running, `grep -E "Wphid|WAprime" UFO_dir/param_card.dat` should show non-trivial widths, and the same values should appear in `proc_dir/Cards/param_card.dat`.
