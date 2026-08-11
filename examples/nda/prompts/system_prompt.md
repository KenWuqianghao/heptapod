# Diagrammatica NDA + FeynGraph Reference

Quick-reference for an LLM agent using the NDA (Naive Dimensional Analysis),
FeynGraph, and MadGraph MCP tools.

## Environment

- **Python**: use the Python executable from your HEPTAPOD environment

## Plotting

When generating matplotlib figures, load the project style at the top of the script:
```python
plt.style.use('heptapod.mplstyle')
```
The style file is in the working directory. It sets LaTeX text rendering, Computer Modern fonts, and publication-quality defaults.

Always save plotting scripts as standalone `.py` files (not inline one-off code) so they can be re-run and modified later. Save all figures as PDF.

**All figures must be publication quality.** Guidelines:
- No arrowed annotations or text callouts on the plot area.
- No panel titles (no `(a) Title`, `(b) Title`, etc.). Sub-panels are labeled in the caption, not on the figure.
- All text (axis labels, tick labels, legend) must be legible at the final printed size — never smaller than the caption font.
- Remove unnecessary gridlines, borders, and legends. If only one series, no legend.
- Less is more: if an element doesn't help the reader interpret the data, remove it.
- Wide aspect ratios for multi-panel figures (`figsize=(width, height)` with width > height).
- Use consistent colors across related figures. Use line style (solid, dashed, dotted) to distinguish series when printed in grayscale.
- Log scales for quantities spanning multiple orders of magnitude. Linear scales otherwise.

## File organization

Keep the sandbox organized. Use subdirectories for different artifact types:

- `scripts/` — computation scripts (`.wl`, `.py`) and their result sidecars (`.json`)
- `figures/` — all generated plots (`.pdf`)
- `output/` — deliverable documents, LaTeX builds, and final reports

Keep the top-level directory clean: only `CLAUDE.md`, `heptapod.mplstyle`, `findings.md`, and subdirectories.

---

## 1. Three Complementary Tools

| | NDA | FeynGraph | MadGraph |
|---|---|---|---|
| **Goal** | Order-of-magnitude width / BR | Diagram enumeration + ranking | Exact tree-level width |
| **Input** | Numerical diagram | Particle labels (SM notation) | MG5 command card |
| **Output** | Width in GeV, scaling formula, BR | Ranked diagrams grouped by class | Exact width or cross section |
| **When** | Rate estimation, sensitivity studies | Counting diagrams, classifying topologies | Validating NDA estimates |

NDA and FeynGraph compose naturally: enumerate diagrams, classify them by
propagator content, then estimate rates for each class. MadGraph provides
independent exact results for cross-checking.

---

## 2. Workflows

### Core workflow: enumerate + classify + estimate

```
1. EnumerateDiagrams(initial=[...], final=[...])
   -> all tree-level diagrams, ranked by importance
   -> grouped into classes by heavy propagator count
   -> saves summary.md with per-class table
   -> returns br_classes array ready for step 2

2. EstimateBranchingRatioNDA(
       diagram_classes=<br_classes from step 1>,
       reference_width=<total width of mother particle>
   )
   -> NDA width per class, branching ratio, summary table
   -> saves nda_br_summary_*.md with per-class breakdown

3. (Optional) EstimatePhaseSpace(mother_mass_gev=<M>, n_body=<N>)
   -> n-body phase space volume

4. (Optional) MadGraphFromRunCard(command_card=<.mg5 file>)
   -> exact width for cross-checking the dominant NDA class
```

### Passing diagrams by reference

The BR tool accepts `diagram_path` as an alternative to inline dicts:
- Path to a JSON file (auto-unwraps EnumerateDiagrams' wrapper)
- Path to a directory (auto-selects `representative.json`)

```json
{
  "diagram_classes": [
    {"diagram_path": "diagrams_.../heavy_0/", "n_diagrams": 84},
    {"diagram_path": "diagrams_.../heavy_1/", "n_diagrams": 42}
  ],
  "reference_width": 2.996e-19
}
```

---

## 3. Diagram Ranking and Class Structure

Diagrams are ranked by **heavy propagator count** — the number of internal
W/Z bosons whose mass $M_W \gg E$ introduces a suppression factor
$(E/M_{\text{prop}})^4$ per propagator in $|\mathcal{M}|^2$. For muon
decay ($E \sim m_\mu$), each additional heavy propagator suppresses the
rate by $(m_\mu/m_W)^4 \sim 10^{-13}$, making the 1-heavy-propagator class
overwhelmingly dominant.

`EnumerateDiagrams` groups diagrams into classes and saves a `summary.md`
in each output directory with a per-class table:

```
| Heavy W | Diagrams | Couplings        |
|:-------:|:--------:|:-----------------|
| 1       | 4        | g_w^2 e^2        |
| 2       | 12       | g_w^4            |
| 3       | 2        | g_w^2 g g_{L_e}  |
```

`EstimateBranchingRatioNDA` saves `nda_br_summary_*.md` files with per-class
NDA widths and branching ratios.

**Build figures and tables directly from this structured output.** The
per-class breakdown is the key data: it reveals which topologies dominate
and by how much. For multiplicity studies, collect per-class data at each
$n$ and build cross-multiplicity comparison figures showing how the class
structure evolves with final-state particle count.

---

## 4. MadGraph Cross-Checks

Write an MG5 command card and pass it to `MadGraphFromRunCard`:

```
set automatic_html_opening False
import model sm-lepton_masses

generate mu- > e- ve~ vm  QED<=4

output ./PROC_NAME
launch

set nevents 0
set lhaid 0
```

Key points:
- `QED<=N` on the `generate` line isolates a specific coupling-order class —
  use this to cross-check the dominant NDA class.
- `set nevents 0` gives the width without generating events.
- Use `sm-lepton_masses` for light lepton decays (default `sm` sets
  $m_\mu = m_e = 0$).
- MadGraph uses different particle names: `nu_mu` → `vm`, `gamma` → `a`,
  `Z` → `z`, `H` → `h`.

---

## 5. Particle Notation

- Quarks: `u`, `d`, `s`, `c`, `b`, `t` (antiparticles: `ubar`, `bbar`, etc.)
- Leptons: `e-`, `mu-`, `tau-` (antiparticles: `e+`, `mu+`, `tau+`)
- Neutrinos: `nu_e`, `nu_mu`, `nu_tau` (antineutrinos: `nu_ebar`, `nu_mubar`, `nu_taubar`)
- Bosons: `H`, `W+`, `W-`, `Z`, `gamma`, `g` (gluon)

---

## 6. Writing Results

For comprehensive results, write a LaTeX document (`.tex`). Reserve markdown
for short summaries and intermediate notes. Write incrementally — append each
result as it is computed, don't wait until the end.

### LaTeX document style

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,booktabs,array,longtable,hyperref,xcolor}
\usepackage{tikz}
\usepackage{caption,subcaption}

% TikZ setup for Feynman diagrams
\pgfdeclarelayer{nodelayer}
\pgfdeclarelayer{edgelayer}
\pgfsetlayers{edgelayer,nodelayer,main}
\tikzstyle{straight}=[-, draw=black, thick]
\tikzstyle{wavy}=[-, draw=black, thick, decorate,
  decoration={snake, amplitude=1.2pt, segment length=5pt}]
\tikzstyle{none}=[]

\title{...}
\author{Tony Menzo and Claude Opus 4.6 (high effort)\\[4pt]
\small Computed with \textsc{Heptapod}}
\date{\today}
```

**Conventions:**
- Tables use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`).
- Number formatting: `$3.2\times10^{-5}$` (never `3.2e-5`).
- **Never use unicode symbols** in `.tex` files. Use LaTeX commands only.
- Include representative Feynman diagrams from each ranked class using
  `output_format="tikz"` on `EnumerateDiagrams`.
