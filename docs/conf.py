# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'homework-3'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
