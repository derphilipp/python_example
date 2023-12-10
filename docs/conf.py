"""Sphinx configuration."""
project = "Python Example"
author = "Philipp Weißmann"
copyright = "2023, Philipp Weißmann"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
