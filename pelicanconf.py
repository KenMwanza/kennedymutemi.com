#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kennedy Mutemi'
SITENAME = u'Kennedy Mutemi'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = u'en'

MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', 'http://kennedymutemi.com/'),
         ('About', 'http://kennedymutemi.com/about.html'),
         ('Projects', 'http://kennedymutemi.com/projects.html'),
         ('Resume', 'http://kennedymutemi.com/resume.html'))

# Social widget
SOCIAL = (('@quizonia', 'https://twitter.com/quizonia/'),
        ('+KennedyMutemi', 'https://plus.google.com/103079388328852575515'),)

DEFAULT_PAGINATION = 10

# Static paths
STATIC_PATHS = ['pdfs']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
