# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Add the parent directory to sys.path so Sphinx can import electroMICA
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# -- Project information -------------------------------------------------------
project = 'electroMICA'
copyright = '2025, MICA Lab at McGill University'
author = 'MICA Lab at McGill University'
release = '1.0.0'

# -- General configuration -----------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

# autosummary generates summary tables for autodoc
autosummary_generate = True

# autodoc options
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    'show-inheritance': True,
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output --------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_static_path = ['_static']
html_logo = '../img/electroMICA_logo.png' if os.path.exists('../img/electroMICA_logo.png') else None

# -- Options for intersphinx -------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'scipy': ('https://docs.scipy.org/doc/scipy', None),
    'pandas': ('https://pandas.pydata.org/docs', None),
    'nibabel': ('https://nipy.org/nibabel', None),
}

# -- Options for LaTeX output -----------------------------------------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'preamble': '',
    'figure_align': 'htbp',
}

latex_documents = [
    ('index', 'electroMICA.tex', 'electroMICA Documentation',
     'MICA Lab at McGill University', 'manual'),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    ('index', 'electromica', 'electroMICA Documentation',
     ['MICA Lab at McGill University'], 1)
]

# -- Options for Texinfo output -----------------------------------------------
texinfo_documents = [
    ('index', 'electroMICA', 'electroMICA Documentation',
     'MICA Lab at McGill University', 'electroMICA',
     'Project EEG features onto cortical and hippocampal surfaces.',
     'Miscellaneous'),
]
