"""
# __init__.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Literature tools: find a paper, get its text, and find what constrains it.

Three layers, each covering what the one before it cannot:

  **Find it.**    ``ArxivSearchTool`` searches arXiv; ``AdsSearchTool`` searches
                  NASA ADS, which reaches published astrophysical and
                  cosmological literature and can search full text. The
                  INSPIRE bundle covers HEP metadata and citations.

  **Read it.**    ``ArxivSourceTool`` fetches the LaTeX e-print, which is the
                  best input for reading a paper's equations because they
                  survive intact. Where arXiv has no source, ``PDFToTeXTool``
                  reconstructs TeX-faithful text from the PDF instead —
                  symbols, sub/superscripts, fractions and radicals come back
                  as TeX macros rather than being flattened away.

  **Check it.**   ``FindExperimentalLimitsTool`` turns a model's field content
                  into searches for papers reporting limits on it, and
                  ``ExtractConstraintsTool`` pulls the numeric bounds out of
                  those papers with the sentence each came from.
"""

from .ads_interface import AdsInterface
from .arxiv_interface import ArxivInterface
from .limits_tools import (
    AdsSearchTool,
    ExtractConstraintsTool,
    FindExperimentalLimitsTool,
)
from .literature_tools import (
    ArxivSearchTool,
    ArxivSourceTool,
    FetchPaperPDFTool,
)
from .pdf_to_tex_tool import PDFToTeXTool
from .tex_extract import pdf_to_tex, page_to_tex

__all__ = [
    # find
    "ArxivSearchTool",
    "AdsSearchTool",
    # read
    "ArxivSourceTool",
    "FetchPaperPDFTool",
    "PDFToTeXTool",
    "pdf_to_tex",
    "page_to_tex",
    # check against experiment
    "FindExperimentalLimitsTool",
    "ExtractConstraintsTool",
    # interfaces
    "ArxivInterface",
    "AdsInterface",
]
