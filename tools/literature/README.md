# Literature tools

TeX-faithful text extraction from LaTeX-produced PDFs.

## Why this exists

For papers with an arXiv e-print, the LaTeX source is authoritative and should
be preferred — nothing recovered from a PDF beats the macros the author
actually typed. This bundle is the fallback for the cases where no source
exists: journal-only records, older papers, internal notes, theses.

## Why naive PDF text extraction fails on physics

A PDF's text layer maps glyphs to Unicode through the font's ToUnicode CMap.
For a TeX document that mapping is *lossy in exactly the places physics lives*:

| what TeX wrote | what the text layer says | why |
|---|---|---|
| `\epsilon` | `ϵ` U+03F5 | `\varepsilon` also lands near here; NFKC merges them |
| `\mu` | `µ` U+00B5 **micro sign** | not Greek mu |
| `\Delta` | `∆` U+2206 **increment** | not Greek Delta |
| `m` (math italic) | `m` U+006D | plain ASCII — indistinguishable from prose |
| `\mathbb{R}` | `R` | plain ASCII |
| `\sqrt` | `p` | the CMEX extensible radical, slot 0x70 |
| `\frac{1}{4}` | `1`, `4` | the bar is a **drawn rectangle**, not a glyph |
| `\bar{\psi}` | `ψ`, `¯` | accent is a separate spacing glyph |

Round-tripping that Unicode back to TeX produces output that looks
authoritative and is wrong — `\epsilon` returns as `\varepsilon`, and `\sqrt`
returns as the letter p.

## How this module works instead

Two sources of information that survive where Unicode does not:

1. **Font identity per glyph.** TeX segregates math by font: `CMMI` is Computer
   Modern Math Italic, so every glyph in it is a variable; `CMSY`/`CMEX` carry
   operators and extensible delimiters; `MSBM` carries blackboard bold. Keying
   on `(font_family, glyph)` recovers `\epsilon` vs `\varepsilon`, `\mathbb{R}`
   from a plain `R`, and the math/prose boundary.

2. **Path objects.** Fraction bars and radical vinculums are filled rectangles.
   Reading them back gives the structure needed to rebuild `\frac{}{}` and
   `\sqrt{}` by partitioning glyphs above/below/left/right of each rule.

3. **Fence geometry.** A matrix's rows sit on separate baselines, so vertical
   clustering splits them; the enclosing delimiter is what says they form one
   expression. Tall fences are either one large glyph or a vertical stack of
   extensible pieces in the private use area (`U+F8EB`, `U+F8EC`, …), so pieces
   sharing a kind, side and column are merged into one fence, openers matched
   to closers by height, and the enclosed glyphs read off as a grid.

Script level is measured against each glyph's **baseline origin**, not its
bounding box — a descender like `p` sits below the baseline, which would
otherwise make its own subscript appear higher than its base.

## The glyph table is derived, not hand-written

`build_table.py` compiles a probe document of ~230 macros under four math-font
packages (Computer Modern, Latin Modern, newtx/Times, mathptmx) and records
what each macro actually rendered to. Regenerate after adding macros:

```bash
python build_table.py        # requires pdflatex; writes tex_table.json
```

Current coverage: 688 entries across 22 font families. `pdflatex` is needed
only to regenerate the table, never to use it.

## Usage

```python
from tools.literature import pdf_to_tex

text = pdf_to_tex("paper.pdf")           # whole document
text = pdf_to_tex("paper.pdf", [0, 1])   # first two pages
```

As an agent tool, `PDFToTeXTool` writes to a file under `base_directory` and
returns the path plus a structural summary, so a long paper does not flood the
agent's context.

## Known limitations

- **`\mathrm` and other upright math styles are unrecoverable.** They render in
  the same font as prose, so nothing distinguishes them. `\mathrm{fb}` comes
  back as `fb`.
- **Matrices work for `pmatrix`, `bmatrix`, `Bmatrix` and `array`** with atomic
  entries. Three cases do not yet:
  - `vmatrix`/`Vmatrix` — at ordinary heights the vertical bars come from the
    symbol font rather than the extension font, and the fence table admits only
    extension fonts (admitting the others would make every paren in running
    prose look like a fence). Their rows flatten.
  - A `\frac` or `\sqrt` **inside a cell** puts its parts on baselines of their
    own and currently reads as extra matrix rows.
  - A big operator inside a tall fence is read as a two-row grid.
- **Multi-line aligned environments** (`align`, `eqnarray`) are not
  reconstructed; their rows become separate output lines.
- **Big-operator limits** (`\sum_{i=0}^{N}` in display style) are read as
  ordinary sub/superscripts rather than limits.
- **Spacing macros** (`\,`, `\quad`) are lost; they leave no glyph.
- **Scanned PDFs have no text layer at all.** This module does no OCR and will
  report that the document is empty.

Output is TeX-*flavoured*, intended for an agent to read and reason over. It is
not guaranteed to compile.

## Testing

```bash
python test_runner.py --component literature
```

Tests compile their fixture from LaTeX source held in the test file, so every
assertion checks against known ground truth. They skip if `pdflatex` is absent.
