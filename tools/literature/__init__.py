"""
# __init__.py is a part of the HEPTAPOD package.
# Copyright (C) 2026 HEPTAPOD authors (see AUTHORS for details).
# HEPTAPOD is licensed under the GNU GPL v3 or later, see LICENSE for details.
# Please respect the MCnet Guidelines, see GUIDELINES for details.

Literature tools.

Extraction of TeX-faithful text from LaTeX-produced PDFs, for papers where no
arXiv source is available.
"""

from .pdf_to_tex_tool import PDFToTeXTool
from .tex_extract import pdf_to_tex, page_to_tex

__all__ = [
    "PDFToTeXTool",
    "pdf_to_tex",
    "page_to_tex",
]
