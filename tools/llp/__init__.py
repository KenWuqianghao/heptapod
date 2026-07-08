"""
# __init__.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Long-lived-particle (LLP) reach tools.

Setting- and model-agnostic tools for decay-in-volume LLP studies:
sampling a weighted LLP flux from an analytic parent-flux kernel
convolved with a DECLARED parent-rest-frame energy spectrum (a pinned
data product — a table or a two-body delta — not a hard-coded
amplitude), and computing signal yields over a lifetime grid (portal g
reweighting or direct ctau) with exact reweighting. The experimental
setting (collider-forward vs beam-dump) lives in the kernel YAML,
geometry YAML, and n_int; the production physics lives in the spectrum
data product — never in the tools.
"""

from .flux_from_meson_decay import LLPFluxFromMesonDecayTool
from .decay_in_volume import DecayInVolumeTool

__all__ = [
    "LLPFluxFromMesonDecayTool",
    "DecayInVolumeTool",
]
