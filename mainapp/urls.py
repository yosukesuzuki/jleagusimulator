# -*- coding: utf-8 -*-
# mainapp.urls
# 

#import urllib

#from google.appengine.api import memcache

from kay.routing import (
  ViewGroup, Rule
)
#from kay.generics import crud
#from kay.generics import admin_required

from kay.exceptions import NotAuthorized
from kay.generics import (
  OP_LIST, OP_SHOW, OP_CREATE, OP_UPDATE, OP_DELETE
)

from kay.generics.rest import RESTViewGroup

#from adminapp.forms import AdminPageForm
from mainapp.models import JPlayerData
from mainapp.views import CACHE_NAME_FOR_TOP_PAGE_RESULTS

def read_only(self, request, operation, obj=None, model_name=None,
        prop_name=None):
    if operation == OP_CREATE or operation == OP_UPDATE or \
            operation == OP_DELETE:
        raise NotAuthorized()


class JDataRESTViewGroup(RESTViewGroup):
    models = ['mainapp.models.JPlayerData']
    fetch_page_size = 1000
    authorize = read_only 

view_groups = [
  JDataRESTViewGroup(),
  ViewGroup(
    Rule('/', endpoint='index', view='mainapp.views.index'),
    Rule('/bad/request/', endpoint='bad_request', view='mainapp.views.bad_request'),
    Rule('/article/<string:key_name>/', endpoint='show_each_article', view='mainapp.views.show_each_article'),
    Rule('/article/', endpoint='article_list', view='mainapp.views.article_list'),
    Rule('/tag/<string:tag_name>/', endpoint='search_by_tag', view='mainapp.views.search_by_tag'),
    Rule('/search/', endpoint='search_by_keyword', view='mainapp.views.search_by_keyword'),
    Rule('/rss/feed/', endpoint='rss_feed', view='mainapp.views.rss_feed'),
    Rule('/<string:key_name>/', endpoint='show_each_page', view='mainapp.views.show_each_page'),
  )
]

