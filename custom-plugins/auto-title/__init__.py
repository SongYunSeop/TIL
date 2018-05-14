# -*- coding: utf-8 -*-

from pelican import signals
from pelican.contents import Static
from bs4 import BeautifulSoup

def content_object_init_handler(content):
    if isinstance(content, Static):
        return
    replace_head_to_title(content)

def replace_head_to_title(content):
    soup = BeautifulSoup(content.content, "html.parser")
    title = soup.find('h1').get_text()
    content.metadata['title'] = title
    content.title = title
    soup.find('h1').decompose()
    replaced_content = str(soup)
    content._content = replaced_content
    content._update_content(replaced_content, content.get_siteurl() + '/' + content.url)

def register():
    signals.content_object_init.connect(content_object_init_handler)
