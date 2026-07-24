"""
# __init__.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Long-lived-particle (LLP) reach tools.

Setting- and model-agnostic tools for decay-in-volume LLP studies, driven by
a Pythia forward flux. The pipeline is three stages, each a BaseTool:

  1. HarvestForwardFluxTool: a Pythia event sample (evtjsonl-1.0) ->
     weighted forward parent-flux files (per-inelastic-collision weights).
  2. MesonDecayToLLPTool: a parent flux + a DECLARED parent-rest-frame LLP
     energy spectrum (a pinned data product -- a table or a two-body delta,
     not a hard-coded amplitude) -> g^2-stripped LLP records carrying a
     decay-in-flight production vertex.
  3. DecayInVolumeVsCouplingTool / DecayInVolumeVsLifetimeTool: LLP records +
     geometry -> signal yields over a coupling grid (portal g^2 reweighting,
     the usual reach scan) or an explicit lab-frame ctau grid (model-agnostic),
     with exact reweighting, the z_prod absorber, off-axis geometry, and a
     selectable two_track / photon / none acceptance.

The experimental setting (collider-forward vs beam-dump) lives in the run
card, geometry YAML, and cross-section normalization; the production physics
lives in the spectrum data product -- never in the tools.
"""

from .harvest_forward_flux import HarvestForwardFluxTool
from .meson_decay_to_llp import MesonDecayToLLPTool
from .decay_in_volume import (
    DecayInVolumeVsCouplingTool,
    DecayInVolumeVsLifetimeTool,
)

__all__ = [
    "HarvestForwardFluxTool",
    "MesonDecayToLLPTool",
    "DecayInVolumeVsCouplingTool",
    "DecayInVolumeVsLifetimeTool",
]
