# Autonomous end-to-end run — HeavyN (arXiv:1602.06957)

Artifacts from a fully unattended `scripts/codex_e2e.sh HeavyN` mission
(2026-07-20): Codex fetched the paper, generated the FeynRules model, ran
validation as background jobs (`submitjob`/`jobstatus`/`jobresult`), repaired
two real defects the checks caught (missing `LBSM` total-Lagrangian symbol;
`ClassName -> N` colliding with Mathematica's built-in `N[...]`), passed the
full chain (UFO + Hermiticity/kinetic/mass + MadGraph import) on round 3, then
ran the blank-slate reverse check and stopped for human review.

| file | what |
|---|---|
| `1602.06957.fr` | final validated model (round 3) |
| `audit.json` | provenance ledger for every stage |
| `reverse/REVIEW.pdf` | **the physicist deliverable** — LaTeX-compiled review package with sign-off block |
| `reverse/REVIEW.md` | pandoc source of the PDF |
| `reverse/reconstruction.md` | blank-slate agent's Lagrangian reconstruction from the sanitized `.fr` |
| `reverse/crosscheck.md` | second fresh agent's term-by-term comparison vs the paper |
| `reverse/sanitized.fr`, `sanitizer_report.json` | exactly what the blind agent saw |

The physics verdict belongs to the human reviewer — nothing here declares the
model correct.
