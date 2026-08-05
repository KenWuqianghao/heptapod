"""Derive a (font-family, glyph-sequence) -> TeX-macro table by compiling a
probe document under several math-font packages and reading back what each
macro actually rendered to. Regenerable; no hand-written encoding tables."""
import ctypes, json, subprocess, os, sys, re
import pypdfium2 as pdfium, pypdfium2.raw as pc

GREEK_L = "alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega".split()
GREEK_U = "Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega".split()
BINOPS  = "pm mp times div cdot ast star circ bullet cap cup vee wedge setminus oplus ominus otimes oslash odot dagger ddagger amalg".split()
RELS    = "leq geq ll gg subset supset subseteq supseteq in ni equiv sim simeq asymp approx cong neq propto perp mid parallel prec succ notin".split()
ARROWS  = "leftarrow rightarrow leftrightarrow Leftarrow Rightarrow Leftrightarrow mapsto longrightarrow hookrightarrow rightharpoonup".split()
MISC    = "partial infty nabla surd top bot angle forall exists neg flat natural sharp ell hbar imath jmath wp Re Im aleph prime emptyset".split()
BIGOPS  = "sum prod int oint coprod bigcup bigcap bigoplus bigotimes".split()
AMS     = "lesssim gtrsim varnothing square blacksquare hslash therefore because".split()
BB      = ["mathbb{%s}" % c for c in "RCZNQ"]
CAL     = ["mathcal{%s}" % c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
RM      = []   # \mathrm renders in the prose font; unrecoverable, and probing it poisons CMR
# radicals at several heights: TeX swaps in taller CMEX glyphs as the box grows
SQRT    = ["sqrt{x}", "sqrt{x^2}", "sqrt{\\frac{a}{b}}", "sqrt{\\frac{\\frac{a}{b}}{c}}"]
ACCENTS = [a + "{x}" for a in "bar hat tilde vec dot ddot check breve acute grave".split()]
LETTERS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

ALL = (GREEK_L + GREEK_U + BINOPS + RELS + ARROWS + MISC + BIGOPS + AMS
       + BB + CAL + RM + SQRT + ACCENTS + LETTERS)

# family -> preamble producing it
FAMILIES = {
    "cm":    r"",                                  # Computer Modern (pdflatex default)
    "lm":    r"\usepackage{lmodern}",              # Latin Modern
    "txmi":  r"\usepackage{newtxtext,newtxmath}",  # Times / newtx (common in REVTeX)
    "ptmx":  r"\usepackage{mathptmx}",             # older Times math
}

def make_tex(preamble):
    body = "\n".join(r"Q%04dQ $%s$\par" % (i, m if (len(m)==1 and m.isalpha()) else "\\"+m)
                     for i, m in enumerate(ALL))
    return (r"\documentclass[12pt]{article}\usepackage{amsmath,amssymb}" + preamble +
            r"\usepackage[margin=0.4in]{geometry}\pagestyle{empty}"
            r"\begin{document}\raggedright " + body + r"\end{document}")

def fontfamily(name):
    """ABCDEF+CMMI10 -> CMMI ; strip subset prefix and design size."""
    n = name.split("+")[-1]
    return re.sub(r"\d+", "", n) or n

def read_glyphs(pdf):
    doc = pdfium.PdfDocument(pdf); seq = []
    for pg in doc:
        tp = pg.get_textpage()
        for i in range(tp.count_chars()):
            c = tp.get_text_range(i, 1)
            if not c.strip(): continue
            buf = ctypes.create_string_buffer(160); fl = ctypes.c_int()
            n = pc.FPDFText_GetFontInfo(tp, i, buf, 160, ctypes.byref(fl))
            seq.append((c, fontfamily(buf.raw[:max(0,n-1)].decode("utf-8","replace"))))
    return seq

def is_tag(seq, i):
    return (i+5 < len(seq) and seq[i][0]=="Q" and seq[i+5][0]=="Q"
            and all(seq[i+k][0].isdigit() for k in range(1,5)))

table = {}   # "FAMILY\x00glyphs" -> macro
radicals = {}
stats = {}
for fam, pre in FAMILIES.items():
    open("p.tex","w").write(make_tex(pre))
    r = subprocess.run(["pdflatex","-interaction=nonstopmode","p.tex"],
                       capture_output=True, text=True)
    if not os.path.exists("p.pdf"):
        print(f"  {fam}: FAILED to compile"); continue
    seq = read_glyphs("p.pdf"); i = 0; n = 0
    while i < len(seq):
        if is_tag(seq, i):
            idx = int("".join(seq[i+k][0] for k in range(1,5))); j = i+6; g = []
            while j < len(seq) and not is_tag(seq, j): g.append(seq[j]); j += 1
            if idx < len(ALL) and g:
                macro = ALL[idx]
                fonts = {f for _, f in g}
                if len(fonts) == 1:                      # single-font glyph run
                    key = f"{g[0][1]}\x00" + "".join(c for c, _ in g)
                    table.setdefault(key, macro); n += 1
                elif macro.startswith("sqrt{"):
                    # radical: leading run in the extension font is the surd
                    lead = [x for x in g if x[1] == g[0][1]]
                    key = f"{g[0][1]}\x00" + "".join(c for c, _ in lead)
                    radicals.setdefault(key, "sqrt"); n += 1
            i = j
        else: i += 1
    stats[fam] = n
    os.remove("p.pdf")
    print(f"  {fam:<6} {n:>3}/{len(ALL)} macros")

json.dump({"symbols": table, "radicals": radicals}, open("tex_table.json","w"), indent=0, ensure_ascii=False, sort_keys=True)
print(f"  radicals: {len(radicals)} -> {sorted(radicals)[:4]}")
fams = sorted({k.split("\x00")[0] for k in table})
print(f"\n{len(table)} entries across {len(fams)} font families:\n  {', '.join(fams)}")
