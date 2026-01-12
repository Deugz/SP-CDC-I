# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CDC'
copyright = '2026, V.Deguin'
author = 'V.Deguin'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
]

bibtex_bibfiles = ["references.bib"]
bibtex_reference_style = "author_year"  # ou "label" si tu veux un style classique

exclude_patterns = ["_build",".ipynb_checkpoints","**/.ipynb_checkpoints",]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_logo = "_static/logos/Label-Ecole-Logo.png"
html_favicon = "_static/logos/Label-Ecole-Logo.png"
templates_path = ["_static/_templates"]

html_theme_options = {
    "external_links": [

    ],
    
    "header_links_before_dropdown": 6, 
    "icon_links": [
        {
            "name": "Drive",
            "url": "https://drive.google.com/drive/folders/1tVEDeNz04hoDiSf5rC6Aa1fWoIU3sYrN?usp=drive_link",
            "icon": "fa-brands fa-google-drive",
        },
        {
            "name": "Calendrier",
            "url": "https://docs.google.com/spreadsheets/d/1NEZJVofrB-r15zuVjQ8gWDN5c8zM6vE1vBBqCKaASKk/edit?usp=drive_link",
            "icon": "fa-regular fa-calendar-days",
        },

    ]

}

html_static_path = ['_static']

html_css_files = ["css/page-layout.css", ]
