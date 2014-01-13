# -*- coding: utf-8 -*-
"""
vapp.views
"""

"""
import logging

from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

"""
import logging
import json
import datetime
import urllib
from werkzeug import Response,redirect

from google.appengine.api import files
from google.appengine.api import memcache
from google.appengine.api import search

from django.utils import html
from django.utils import feedgenerator

from kay.utils import render_to_response
from kay.utils import get_by_key_name_or_404
from kay.utils import url_for 
from kay.utils.paginator import Paginator, InvalidPage, EmptyPage
from kay.i18n import gettext as _
from kay.auth.decorators import admin_required
from settings import DEFAULT_LANG

from mainapp.markdown2 import markdown
from mainapp.models import AdminPage,BlobStoreImage,Article,JLeagueRank,JLeagueTeam,JPlayerData

TARGET2014 = 18
GK_DEFENCE_RATE = 1.417
GOAL_POINT_BASE = 70
# Create your views here.

def index(request):
    return render_to_response('vapp/index.html', {'message': 'Hello'})

def get_node_data():
    rank_results = JLeagueRank.all().order('rank').fetch(1000)
    nodes = []
    for rr in rank_results:
        nodes.append({'name':rr.team.key().name(),'id':rr.rank - 1,'point':rr.point,'goal_get':rr.goal_get,
            'goal_lost':rr.goal_lost,'goal_point':rr.goal_point,'base_value':rr.goal_point+GOAL_POINT_BASE})
        nodes.append({'name':rr.team.key().name(),'id':rr.rank - 1 + 19})
    nodes.append({'name':u'その他','id':18})
    nodes.append({'name':u'その他','id':18+19})
    return nodes

def get_trade_player_data():
    rank_results = JLeagueRank.all().order('rank').fetch(1000)
    out_players = []
    for rr in rank_results:
        players = JPlayerData.all().filter(u'old_team =',rr.team.key().name()).fetch(1000)
        for op in players:
            if op.game_count < 1:
                continue
            if op.goal_get < 1 and op.assist < 1 and op.player_type != 'GK':
                continue
            logging.info(op.new_team)
            new_team = JLeagueTeam.get_by_key_name(op.new_team)
            if new_team is None or new_team.j_class != 'J1':
                new_team_target = 37 
                new_team_name = u'その他'
            else:
                logging.info(new_team.team_id)
                new_team_target_entity = JLeagueRank.get_by_key_name(new_team.team_id+'2013')
                new_team_target = new_team_target_entity.rank - 1 + 19  
                new_team_name = new_team.key().name() 
            out_players.append({'name':op.title,'source':rr.rank - 1,'target':new_team_target,'old_team':op.old_team,'new_team':new_team_name,
                'player_type':op.player_type,'game_count':op.game_count,'goal_get':op.goal_get,'assist':op.assist,
                'goal_lost':op.goal_lost,'save_ratio':op.save_ratio,'j_class':'J1'})
        new_players = JPlayerData.all().filter(u'new_team =',rr.team.key().name()).fetch(1000)
        for op in new_players:
            old_team= JLeagueTeam.get_by_key_name(op.old_team)
            #旧チームがJ1の場合は重複排除でスキップ
            if old_team and old_team.j_class == 'J1':
                continue
            old_team_name = u'その他'
            source = 18
            #旧チームがJではない場合
            if old_team is None:
                j_class = op.trade_comment
            #旧チームがJ2のとき
            elif old_team.j_class == 'J2':
                j_class = 'J2'
            out_players.append({'name':op.title,'source':source,'target':rr.rank + - 1 + 19,'old_team':old_team_name,'new_team':rr.team.key().name(),
                'player_type':op.player_type,'game_count':op.game_count,'goal_get':op.goal_get,'assist':op.assist,
                'goal_lost':op.goal_lost,'save_ratio':op.save_ratio,'j_class':j_class})
    return out_players

def trade_data(request):
    memcache_key = 'trade_data'
    data = memcache.get(memcache_key)
    if data:
        return Response(json.dumps(data))
    data = {'nodes':get_node_data(),'links':get_trade_player_data()}
    memcache.set(memcache_key,data)
    return Response(json.dumps(data))
    
