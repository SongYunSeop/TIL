#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import glob

AUTHOR = 'Yunseop Song'
SITENAME = '전지적 송윤섭시점 TIL'
SITEURL = ''

ARTICLE_PATHS = glob.glob(os.getcwd()+"/*/*.md")
# ARTICLE_PATHS.append(os.getcwd()+"/README.md")

OUTPUT_PATH = 'public/'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Blog', 'https://songyunseop.com/'),
    ('Tech', 'https://tech.songyunseop.com/'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY='TIL'
USE_FOLDER_AS_CATEGORY=True
DISPLAY_PAGES_ON_MENU=False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_DATE = (2018, 1, 1)
FILENAME_METADATA = '(?P<title>.*)'

DISQUS_SITENAME = 'songyunseop'
GITHUB_URL = 'https://github.com/songyunseop/til'
