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
            "url": "https://drive.google.com/drive/folders/1Gqv0_RDXwI7om8ob1uVuu7__oYLtDHYp",
            "icon": "fa-brands fa-google-drive",
        },
        {
            "name": "Calendrier",
            "url": "https://calendar.google.com/calendar/embed?height=600&wkst=1&ctz=Europe%2FParis&showPrint=0&mode=WEEK&hl=fr&src=dmRlZ3VpbkBsYWJlbC1lbW1hdXMuY28&src=Y185OWQ3Y2M0MWJhYjE4OTBlYWYyY2FhZmJjZDZjYWZiN2ZjMWRiNmZkYzI1Y2UwYmQ0ZTgzMGFmNzkwZmU1YTgxQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20&src=ZW4uZnJlbmNoI2hvbGlkYXlAZ3JvdXAudi5jYWxlbmRhci5nb29nbGUuY29t&src=bG1lcmVzc2VAbGFiZWwtZW1tYXVzLmNv&color=%230B8043&color=%234285F4&color=%230B8043&color=%23AD1457",
            "icon": "fa-regular fa-calendar-days",
        },

    ]

}

html_static_path = ['_static']

html_css_files = ["css/page-layout.css", ]
