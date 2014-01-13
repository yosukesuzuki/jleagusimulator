# -*- coding: utf-8 -*-
# vapp.urls
# 

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='vapp.views.index'),
    Rule('/trade/data/', endpoint='trade_data', view='vapp.views.trade_data'),
  )
]

