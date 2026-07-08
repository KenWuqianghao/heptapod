"""
# __init__.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Long-lived-particle (LLP) reach tools.

Setting-agnostic tools for decay-in-volume LLP studies: sampling a
weighted LLP flux from an analytic parent-flux kernel convolved with a
declared 3-body production spectrum, and computing signal yields over a
coupling grid with exact g^2 reweighting. The experimental setting
(collider-forward vs beam-dump) lives entirely in the kernel YAML,
geometry YAML, and n_int normalization — never in the tools.
"""

from .flux_from_meson_decay import LLPFluxFromMesonDecayTool
from .decay_in_volume import DecayInVolumeTool

__all__ = [
    "LLPFluxFromMesonDecayTool",
    "DecayInVolumeTool",
]
