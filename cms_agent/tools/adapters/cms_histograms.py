"""Stub adapter: coffea/awkward histogramming for CMS nano-like tables."""

from __future__ import annotations

from typing import Any, Mapping


def build_leading_pt_histogram(table: Mapping[str, Any], field_pt: str = "Photon_pt") -> dict[str, Any]:
    """
    Real implementation would use coffea/hist; this stub documents the contract.

    Parameters
    ----------
    table :
        Awkward/Coffea-compatible event table (not materialized here).
    field_pt :
        Column storing photon transverse momentum in GeV.

    Returns
    -------
    dict
        JSON-serializable histogram representation + optional PNG path.
    """
    raise NotImplementedError("Wire coffea processor + schema validation in a CMS environment.")
