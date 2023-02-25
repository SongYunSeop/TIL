extensions = ["sphinx_markdown_tables", "sphinx_sitemap", "myst_parser"]

templates_path = ["_templates"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}


master_doc = "index"

project = "전지적 송윤섭시점 TIL"
copyright = "2023, Yunseop Song"
author = "Yunseop Song"
github_project_name = "TIL"

version = "1.0"
release = "1.0"

language = "en"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".idea"]

pygments_style = "sphinx"

todo_include_todos = False

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
    "collapse_navigation": False,
    "display_version": False,
    "navigation_depth": 3,
}

html_context = {
    "display_github": True,
    "github_user": "songyunseop",
    "github_repo": github_project_name,
    "github_version": "master",
    "conf_py_path": "/",
    "source_suffix": source_suffix,
}

html_static_path = []

html_sidebars = {
    "**": [
        "relations.html",  # needs 'show_related': True theme option to display
        "searchbox.html",
    ]
}
htmlhelp_basename = "TILdoc"
latex_elements = {}
latex_documents = [
    (master_doc, "TIL.tex", "TIL Documentation", "Yunseop Song", "manual"),
]
man_pages = [(master_doc, "til", "TIL Documentation", [author], 1)]
texinfo_documents = [
    (
        master_doc,
        "TIL",
        "TIL Documentation",
        author,
        "TIL",
        "One line description of project.",
        "Miscellaneous",
    ),
]

site_url = "https://til.songyunseop.com/"
