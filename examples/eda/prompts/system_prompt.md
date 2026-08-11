# Diagrammatica Reference

Quick-reference for an LLM agent using the NDA (Naive Dimensional Analysis),
FeynGraph, and EDA (Exact Diagrammatic Analysis) MCP tools.

## Environment

- **Python**: use the Python executable from your HEPTAPOD environment

## Plotting

When generating matplotlib figures, load the project style at the top of the script:
```python
plt.style.use('heptapod.mplstyle')
```
The style file is in the working directory. It sets LaTeX text rendering, Computer Modern fonts, and publication-quality defaults.

Prefer fewer, denser figures that show relationships between quantities over many single-variable plots. Always save plotting scripts as standalone `.py` files (not inline one-off code) so they can be re-run and modified later. Save all figures as PDF.

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

## 1. Two Calculation Paths

| | NDA path (numerical) | EDA path (symbolic-first) |
|---|---|---|
| **Goal** | Order-of-magnitude estimate | Exact tree-level formula |
| **Input** | Numerical diagram (masses + couplings as numbers) | Symbolic diagram (labels + vertex types, no numbers) |
| **Engine** | Python dimensional analysis | FeynCalc via wolframscript |
| **Output** | Width in GeV + scaling formula | Symbolic expression Γ(M, m, g) |
| **When** | Quick check, sanity test, compare diagrams | Paper-ready result, parameter scans |

---

## 2. Workflows

### EDA path: symbolic-first

```
1. Build symbolic diagram dict (labels + vertex type + spins, no masses/couplings)

2. ComputeSymbolicAmplitude(diagram=<above>)
   -> generates a complete .wl script (traces, spin sums, phase space — all included)
   -> returns script_path

3. RunWolframScript(script_path=<script_path from step 2>)
   -> executes the generated script as-is — do not modify or rewrite it
   -> returns SYMBOLIC_RESULT[width], saves _results.json sidecar

   For multiple diagrams: call ComputeSymbolicAmplitude for each to collect
   script_paths, then RunWolframScriptBatch(script_paths=[...]) to execute
   all concurrently in a single MCP call.

4. (Optional) SimplifyResult(script_path=<from step 3>, result_name="width",
       substitutions={"mfbar": "mf"}, limit={"var": "mf", "point": "0"})
   -> applies substitutions, limits, series, simplification via wolframscript
   -> saves its own _results.json sidecar for downstream chaining

   For multiple limits/substitutions on the same expression:
   SimplifyResultBatch(specs=[{script_path, result_name, substitutions, ...}, ...])
   -> runs all simplifications concurrently in a single MCP call

5. ConvertToPython(script_path=<from step 3 or 4>, result_name="width" or "simplified")
   -> reads the _results.json sidecar automatically
   -> returns Python source code for the function
   -> optionally evaluates at given values
```

**Scope**: ComputeSymbolicAmplitude generates code for all $1 \to 2$ and $2 \to 2$
topologies with these vertex families:

- **SFF** (scalar–fermion–fermion): yukawa, pseudoscalar, chiral, scalar-va
- **VFF** (vector–fermion–fermion): vector, axial-vector, left/right-handed, va, chiral, tensor/dipole
- **Bosonic**: SSS, SSV, SVV, VVV (dispatched by spin, any type string works)
- **Dim-5 SVV**: field-strength ($\phi F F$), dual-field-strength ($\phi F \tilde{F}$)

For effective operators not listed above (dim6-4fermion, dim5-weinberg), use
the NDA path instead.

**In-script simplifications**: Instead of a separate SimplifyResult call,
you can pass `simplifications` directly to ComputeSymbolicAmplitude:
```json
{
  "simplifications": {
    "substitutions": {"mfbar": "mf"},
    "limit": {"var": "mf", "point": "0"},
    "simplify": "Simplify",
    "assumptions": ["M > 0"]
  }
}
```

### Fermion-parent example

For decays like f₁ → S f̄₂:
```json
{
  "initial": [{"label": "f1", "spin": "1/2"}],
  "final": [{"label": "S", "spin": 0}, {"label": "f2bar", "spin": "1/2"}],
  "vertices": [{"type": "scalar-va"}]
}
```
The tool assigns spinors based on particle position and the antiparticle
heuristic (labels ending in `bar`, `~`, or `+` are antiparticles).

### NDA path: numerical estimate

```
1. Build numerical diagram dict (masses, couplings, spins all specified)

2. EstimateDecayWidthNDA(diagram=<above>)
   -> width_gev (best estimate), method, formula
```

### SM diagram enumeration

```
EnumerateDiagrams(initial=["H"], final=["b", "bbar"])
-> all contributing diagrams, ranked by importance
-> feed dominant diagram into NDA or EDA path
```

### Branching ratio workflow (enumerate → classify → BR)

```
1. EnumerateDiagrams(initial=[...], final=[...], metadata_only=True)
   -> returns classes with representative diagrams + counts
   -> includes a "br_classes" array ready for step 3

2. Compute reference total width (EstimateDecayWidthNDA on dominant channel,
   or use an experimental value from PDGDatabase)

3. EstimateBranchingRatioNDA(
       diagram_classes=<br_classes from step 1>,
       reference_width=<from step 2>)
   -> branching ratio for each class + total BR
```

**Passing diagrams by reference**: The BR tool accepts `diagram_path` as an
alternative to inline `diagram` dicts. Supported formats:
- Path to a JSON file (auto-unwraps EnumerateDiagrams' `{"rank": N, "diagram": {...}}` wrapper)
- Path to a directory (auto-selects `representative.json` or the top-ranked file)

Example using by-path:
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

## 3. Output Conventions

`SYMBOLIC_RESULT[width]` is the full partial decay width (spin-averaged,
color factor included, identical-particle symmetry factor included).

`SYMBOLIC_RESULT[ampSq]` is the spin-summed squared amplitude before phase space.

### Complex couplings

By default, couplings are treated as complex. Results contain `Conjugate[g]`
terms. Set `assume_real_couplings: true` on ComputeSymbolicAmplitude for
simpler $g^2$ expressions.

---

## 4. Diagram Format

### Numerical Diagram (NDA path)

All masses, spins, and coupling values must be provided as numbers.

```json
{
  "topology": "tree_2body",
  "initial": [{"label": "S", "spin": 0, "mass": 500.0}],
  "final": [
    {"label": "f", "spin": "1/2", "mass": 5.0},
    {"label": "fbar", "spin": "1/2", "mass": 5.0}
  ],
  "vertices": [{"type": "yukawa", "coupling": "y"}],
  "couplings": {"y": 0.1},
  "color_factor": 1.0
}
```

### Symbolic Diagram (EDA path)

Labels + vertex types + spins required. Masses and coupling values are left as symbols.

```json
{
  "topology": "tree_2body",
  "initial": [{"label": "S", "spin": 0}],
  "final": [
    {"label": "f", "spin": "1/2"},
    {"label": "fbar", "spin": "1/2"}
  ],
  "vertices": [{"type": "yukawa", "coupling": "y"}]
}
```

### Key fields

- `spin`: accepts `0`, `0.5`, `1`, `"1/2"`, `"scalar"`, `"fermion"`, `"vector"`.
  Spin-1 defaults to **massive**. For massless vectors, set `"massive": false`.
- `topology`: auto-inferred if omitted.
- `color_factor`: default 1.0; set to 3.0 for quark final states.
- `propagators[].regime`: `"auto"` (default), `"heavy"`, `"light"`.

---

## 5. Vertex Type System

Vertex type names are unified across both paths — the same names work for
ComputeSymbolicAmplitude and EstimateDecayWidthNDA.

### SFF (scalar–fermion–fermion)

| type | coupling format | FeynCalc structure |
|---|---|---|
| `"yukawa"` / `"scalar"` | string or number | `I g` |
| `"pseudoscalar"` | string or number | `I g GA[5]` |
| `"chiral"` / `"scalar-chiral"` | `{"gL": ..., "gR": ...}` | `I (gL GA[7] + gR GA[6])` |
| `"scalar-va"` | `{"gS": ..., "gP": ...}` | `I (gS + gP GA[5])` |

### VFF (vector–fermion–fermion)

| type | coupling format | FeynCalc structure |
|---|---|---|
| `"vector"` / `"gauge-vector"` | string or number | `I g GAD[mu]` |
| `"axial-vector"` | string or number | `I gA GAD[mu] . GA[5]` |
| `"left-handed"` | string or number | `I g GAD[mu] . GA[7]` |
| `"right-handed"` | string or number | `I g GAD[mu] . GA[6]` |
| `"vector-axial"` / `"va"` | `{"gV": ..., "gA": ...}` | `I GAD[mu] . (gV - gA GA[5])` |
| `"chiral"` / `"vector-chiral"` | `{"gL": ..., "gR": ...}` | `I GAD[mu] . (gL GA[7] + gR GA[6])` |
| `"tensor"` / `"dipole"` | string or number | `I g sigma^{mu nu} k_nu` |
| `"tensor-chiral"` / `"dipole-chiral"` | `{"gL": ..., "gR": ...}` | `I (gL GA[7] + gR GA[6]) . sigma^{mu nu} k_nu` |

### Bosonic (SSS, SSV, SVV, VVV)

Codegen dispatches by **spin configuration**, not vertex type name.

| spin config | parent | daughters | FeynCalc structure |
|---|---|---|---|
| [0,0,0] SSS | scalar | scalar + scalar | `I g` |
| [0,0,1] SSV | vector | scalar + scalar | `I g ε·(p₁ - p₂)` |
| [0,1,1] SVV | scalar | vector + vector | `I g ε₁·ε₂` (default) |
| [0,1,1] SVV | vector | scalar + vector | `I g ε₀·ε₁` |
| [1,1,1] VVV | vector | vector + vector | triple gauge: `g(ε·p)` terms |

### Dim-5 SVV operators ($\phi FF$ / $\phi F \tilde{F}$)

| type | aliases | FeynCalc structure |
|---|---|---|
| `"field-strength"` | `"dim5-FF"` | `2ig [(k₁·k₂)(ε₁·ε₂) - (k₁·ε₂)(k₂·ε₁)]` |
| `"dual-field-strength"` | `"dim5-FF-dual"` | `2g ε^{μνρσ} k₁_ρ k₂_σ ε₁_μ ε₂_ν` |

### EFT operators (NDA only, no codegen)

| type | coupling format |
|---|---|
| `"dim6-4fermion"` | number (G_F in GeV^-2) |
| `"dim5-weinberg"` | number (1/Lambda in GeV^-1) |

### Coupling defaults

If `coupling` is omitted, a default is inferred:

| type | default coupling |
|---|---|
| `"chiral"` / `"scalar-chiral"` / `"vector-chiral"` / `"tensor-chiral"` | `{"gL": "gL", "gR": "gR"}` |
| `"vector-axial"` / `"va"` | `{"gV": "gV", "gA": "gA"}` |
| `"scalar-va"` | `{"gS": "gS", "gP": "gP"}` |
| everything else | `"g"` |

---

## 6. Particle Notation

- Quarks: `u`, `d`, `s`, `c`, `b`, `t` (antiparticles: `ubar`, `bbar`, etc.)
- Leptons: `e-`, `mu-`, `tau-` (antiparticles: `e+`, `mu+`, `tau+`)
- Neutrinos: `nu_e`, `nu_mu`, `nu_tau` (antineutrinos: `nu_ebar`, `nu_mubar`, `nu_taubar`)
- Bosons: `H`, `W+`, `W-`, `Z`, `gamma`, `g` (gluon)

Antiparticle heuristic: labels ending in `bar`, `~`, or `+` (for leptons).

---

## 7. Tool Chaining

EDA tools accept input **by reference** (`script_path` + `result_name`) — they
read the `_results.json` sidecar automatically. No manual expression copying.

SimplifyResult transformation order: `substitutions` → `limit` → `series` →
`assumptions` + `simplify`. Calls can be chained: output sidecar from one
becomes input to the next.

### Mathematica precedence pitfall

In hand-written RunWolframScript code, `-` binds **tighter** than `/.`:
```
(* WRONG *)  diff = FullSimplify[widthVA /. subRules - widthChiral];
(* RIGHT *)  diff = FullSimplify[(widthVA /. subRules) - widthChiral];
```

### MCP concurrency

The MCP client serializes requests per server. For systematic sweeps, use
batch tools (`RunWolframScriptBatch`, `SimplifyResultBatch`) to run all work
in a single MCP call.

---

## 8. Writing Summaries

For comprehensive results, write a LaTeX document (`.tex`). Reserve markdown
for short summaries and intermediate notes.

### LaTeX document style

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,booktabs,array,longtable,hyperref,xcolor}

\newcommand{\Msq}{\overline{|\mathcal{M}|^2}}
\newcommand{\la}{\lambda}
\DeclareMathOperator{\Tr}{Tr}

\title{...}
\author{Tony Menzo and Claude Opus 4.6 (high effort)\\[4pt]
\small Computed with \textsc{Heptapod}}
\date{\today}
```

**Conventions:**
- Tables use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`).
- Number formatting: `$3.2\times10^{-5}$` (never `3.2e-5`).
- **Never use unicode symbols** in `.tex` files. Use LaTeX commands only
  (`\Gamma`, `\alpha`, `\to`, `\times`, `_1`, `^2`).
- Use `LATEX_RESULT[...]` output from tools directly — symbol cleanup is automatic.

### Write incrementally

Append each result to the summary as it is computed. Do not wait until the
end of a session.

### NDA sanity checks

When computing exact results via the EDA path, consider running an NDA
estimate on the final width as a cross-check.
