# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '4.A'
copyright = '2026, V.Deguin'
author = 'V.Deguin'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

numfig = True

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.bibtex",
    "sphinx_new_tab_link",
    "hoverxref.extension",
]

myst_enable_extensions = [
    "colon_fence",
    "linkify",
]

hoverxref_auto_ref = True
hoverxref_domains = ["std"]  # important pour les :term:
hoverxref_roles = [
    "term",
]
hoverxref_role_types = {
    "term": "tooltip",
    "ref": "tooltip",
}

hoverxref_tooltip_content = "text"

bibtex_bibfiles = ["references.bib"]
bibtex_reference_style = "author_year"  # ou "label" si tu veux un style classique

exclude_patterns = ["_build",".ipynb_checkpoints","**/.ipynb_checkpoints",]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo/Under_construction.svg"
html_favicon = "_static/logo/Under_construction.svg"
templates_path = ["_static/_templates"]

html_theme_options = {
    "navigation_with_keys": True,
    "show_toc_level": 2,
    "external_links": [

    ],
    
    "header_links_before_dropdown": 7, 
    "icon_links": [
        {
            "name": "Framaspace",
            "url": "https://4-a.frama.space/",
            "icon": "fa-solid fa-cloud",
        },
    ],

    "logo": {
        "text": " &nbsp <strong>4.A Doc</strong> - <em> in progress</em> ",
        "alt_text": "en construction",
    },

}

html_static_path = ['_static']

html_css_files = ["css/page-layout.css", "css/page-content.css", "css/admonition-style.css"]
