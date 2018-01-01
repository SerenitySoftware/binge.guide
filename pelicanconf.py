#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bingeworthy'
SITENAME = u'The Binge Guide'
SITEURL = ''
THEME = 'theme/binge'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

ARTICLE_URL = '/{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '/{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = '/genre/{slug}/'
TAG_SAVE_AS = 'genre/{slug}/index.html'

def bingeworthy_sort(article):
    return 100 - int(article.metadata["bingeworthy"])

ARTICLE_ORDER_BY = bingeworthy_sort

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
