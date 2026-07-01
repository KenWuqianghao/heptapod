"""
# benchmarks.py is a part of the HEPTAPOD package.
# Copyright (C) 2025 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Benchmark cases for the Lagrangian-extraction pipeline.

Each case is scored on how well extraction recovers the model's new-particle
content and quantum numbers (the robust ground-truth signal), and whether the
generated .fr validates end to end. Charges are rational strings, matching the
schema. `paper_text` (inline) lets a case run without network; `arxiv_id` lets
the runner fetch the paper instead.
"""

BENCHMARKS = [
    {
        "name": "scalar_leptoquark_S1",
        "scenario": "Scalar leptoquark S1 ~ (3, 1, -1/3), first generation, "
        "coupling to a right-handed up quark and right-handed charged lepton.",
        "paper_text": (
            "We add to the Standard Model a scalar leptoquark S1 transforming as "
            "(3, 1, -1/3) under SU(3)c x SU(2)L x U(1)Y. It is a colour triplet, "
            "weak singlet, with electric charge Q = -1/3. We take its mass to be "
            "MS1 = 1500 GeV. The relevant interaction is a right-handed Yukawa "
            "coupling y_RR between S1, a right-handed up quark and a right-handed "
            "charged lepton, giving the decay S1 -> e- u and QCD pair production "
            "pp -> S1 S1~."
        ),
        "expected": {
            "particles": [{"name": "S1", "charge": "-1/3"}],
            "parameters": [],
        },
    },
    {
        "name": "two_higgs_doublet_model",
        "scenario": "Two-Higgs-Doublet Model (2HDM) type-II: a second scalar "
        "doublet giving physical states h, H (CP-even), A (CP-odd), and H+/-.",
        "arxiv_id": "1106.0034",  # Branco et al., 2HDM theory and phenomenology
        "expected": {
            "particles": [
                {"name": "H", "charge": "0"},
                {"name": "A", "charge": "0"},
                {"name": "H+", "charge": "1"},
            ],
            "parameters": [],
        },
    },
    {
        "name": "scalar_singlet_dark_matter",
        "scenario": "Scalar singlet dark matter: a real gauge-singlet scalar S "
        "(Z2-odd, electrically neutral) with a Higgs-portal coupling.",
        "arxiv_id": "1306.4710",  # scalar singlet DM (representative)
        "expected": {
            "particles": [{"name": "S", "charge": "0"}],
            "parameters": [],
        },
    },
]
