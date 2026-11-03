# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import pathlib
import tomllib
from datetime import datetime

docroot = pathlib.Path(__file__).parent
pyproject_toml = docroot.parent.joinpath("pyproject.toml")
project_info = tomllib.loads(pyproject_toml.read_text())["project"]


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "SARCalNet"
author = ", ".join(author["name"] for author in project_info["authors"])
copyright = f"{datetime.now():%Y}, {author}"

version = project_info["version"]
release = version


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    # "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    # "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = {
    ".rst": "restructuredtext",
}
root_doc = "index"
language = "en"
nitpicky = True
# nitpick_ignore = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_title = f"{project} Documentation"
html_short_title = project
html_logo = "_static/logo/sarcalnet-logo.png"
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_search_language = "en"
html_show_sourcelink = False

html_theme_options = {
    # Header
    "navbar_end": [
        "search-field",
        "theme-switcher",
        "navbar-icon-links",
    ],
    # SARCalNet logo
    "logo": {
        "text": project,
        "image_light": "_static/logo/sarcalnet-logo.png",
        "image_dark": "_static/logo/sarcalnet-logo-dark.png",
        "alt_text": project,
    },
    # External links
    "icon_links": [
        {
            "name": "SARCalNet website",
            "url": "https://www.sarcalnet.org/",
            "icon": "fa-solid fa-globe",
            "type": "fontawesome",
        },
        {
            "name": "CEOS WGCV SAR Subgroup",
            "url": "https://calvalportal.ceos.org/sar_subgroup",
            "icon": "fa-solid fa-satellite",
            "type": "fontawesome",
        },
    ],
    # Footer
    "footer_start": [
        "copyright",
    ],

    "footer_end": [
        "sphinx-version",
        "theme-version",
    ],
}
html_context = {
    # "default_mode": "light",
    "github_user": "sarcalnet",
    "github_repo": "sarcalnet-docs",
    "github_version": "main",
    "doc_path": "docs",
}


# -- Options for autosectionlabel extension ----------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html

autosectionlabel_prefix_document = True


# -- Options for extlinks extension ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#module-sphinx.ext.extlinks

extlinks = {
    "sarcalnet": (
        "https://www.sarcalnet.org/%s",
        "SARCalNet: %s",
    ),
}

# -- Options for sphinx-cioybutton extension ---------------------------------
# https://sphinx-copybutton.readthedocs.io

copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
