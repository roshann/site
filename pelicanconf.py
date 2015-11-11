#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Roshan Nair'
SITENAME = u'Blog'
SITESUBTITLE = u'Tour subtitle of tag line' #optional
SITEURL = ''

# Send index.html template to blog.html, since we have configured
# about.html to be saved as index.html
# see - http://docs.getpelican.com/en/3.6.3/faq.html#how-can-i-use-a-static-page-as-my-home-page
INDEX_SAVE_AS = 'blog.html'

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

THEME = "themes/flasky"

DEFAULT_LANG = u'en'

# Navigation sections and relative URL:
SECTIONS = [
        #('Blog', 'index.html'),
        ('About', 'index.html')
        #('Blog', 'blog.html')
        #('Archive', 'archives.html'),
        #('Tags', 'tags.html'),
        #('Projects', 'pages/projects.html'),
        #('Talks', 'pages/talks.html'),
        ]

# Feed generation is usually not desired when developing
DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
        'en': '%d %m %Y'
        }
DEFAULT_DATE_FORMAT = '%d %m %Y'
DEFAULT_PAGINATION = 10
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

OUTPUT_PATH = 'output'
# static paths will be copied under the same name
STATIC_PATHS = ["images"]

# Optional social media links
# =============================
#DISQUS_SITENAME = "your_disqus_user"
TWITTER_USERNAME = 'technologic'
LINKEDIN_URL = 'https://in.linkedin.com/in/roshan-nair-89388631'
#GITHUB_URL = 'http://github.com/you'
#FACEBOOK_URL = 'http://www.facebook.com/you'
#GOOGLEPLUS_URL = 'https://plus.google.com/your_profile_id/posts'
#PINTEREST_URL = 'http://pinterest.com/you'
MAIL_USERNAME = 'roshan.nair'
MAIL_HOST = 'gmail.com'

# Optional analytic trackers
# =============================
#GOOGLE_ANALYTICS_ACCOUNT = 'UA-00000000-1'
#PIWIK_URL = 'myurl.com/piwik'
#PIWIK_SSL_URL = 'myurl.com/piwik'
#PIWIK_SITE_ID = '1'

# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
