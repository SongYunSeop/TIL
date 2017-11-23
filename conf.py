#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from recommonmark.parser import CommonMarkParser

extensions = []

templates_path = ['_templates']

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst', '.md']

master_doc = 'index'

project = 'TIL'
copyright = '2017, Yunseop Song'
author = 'Yunseop Song'

version = '1.0'
release = '1.0'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'navigation_depth': 3,
}
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}
htmlhelp_basename = 'TILdoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'TIL.tex', 'TIL Documentation',
     'Yunseop Song', 'manual'),
]
man_pages = [
    (master_doc, 'til', 'TIL Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'TIL', 'TIL Documentation',
     author, 'TIL', 'One line description of project.',
     'Miscellaneous'),
]
