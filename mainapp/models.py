# -*- coding: utf-8 -*-
# mainapp.models

from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.api import images

from kay.auth.models import GoogleUser
from kay.i18n import gettext as _
# Create your models here.

class Article(db.Model):
    '''
    article contents,add and update like a blog
    '''
    display_page_flg = db.BooleanProperty(verbose_name=_('Display this page'),default=False)
    display_time = db.DateTimeProperty(verbose_name=_('Display time,UTC'))
    title = db.StringProperty(verbose_name=_('Title'),required=True,indexed=False)
    url = db.StringProperty(verbose_name=_('Url,page identifier of this content,only at first time'),indexed=False)
    page_order = db.IntegerProperty(verbose_name=_('Page order'),default=99999)
    content = db.TextProperty(verbose_name=_('Content'))
    tags_string = db.StringProperty(verbose_name=_('Tags,comma separated'),indexed=False)
    tags = db.StringListProperty(verbose_name=_('Tag list,for search'))
    images = db.TextProperty(verbose_name=_('Images,JSON Format'))
    lang = db.StringProperty(verbose_name=_('Content Language'))
    external_url = db.StringProperty(verbose_name=_('External Url,If link to an outside page,optional'),indexed=False)
    update = db.DateTimeProperty(verbose_name=_('Update'),auto_now=True)
    created = db.DateTimeProperty(verbose_name=_('Created'),auto_now_add=True)


class AdminPage(db.Model):
    '''
    top page setting and general pages administration,
    If admin set Url field, url is set as key name or escaped Title String is set as key name
    '''
    display_page_flg = db.BooleanProperty(verbose_name=_('Display this page'),default=False)
    title = db.StringProperty(verbose_name=_('Title'),required=True,indexed=False)
    url = db.StringProperty(verbose_name=_('Url,page identifier of this content,only at first time'),indexed=False)
    page_order = db.IntegerProperty(verbose_name=_('Page order'),default=99999)
    content = db.TextProperty(verbose_name=_('Content'))
    images = db.TextProperty(verbose_name=_('Images,JSON Format'))
    lang = db.StringProperty(verbose_name=_('Content Language'))
    external_url = db.StringProperty(verbose_name=_('External Url,If link to an outside page,optional'),indexed=False)
    update = db.DateTimeProperty(verbose_name=_('Update'),auto_now=True)
    created = db.DateTimeProperty(verbose_name=_('Created'),auto_now_add=True)

class BlobStoreImage(db.Model):
    '''
    Blobstore Image Management
    '''
    title = db.StringProperty(verbose_name=_('Title'),default='',indexed=False)
    file_name = db.StringProperty(verbose_name=_('File Name'),default='',indexed=False)
    note = db.TextProperty(verbose_name=_('Note'),default='',indexed=False)
    blob_key = blobstore.BlobReferenceProperty()
    image_path = db.StringProperty(verbose_name=_('Image Path'),default='',indexed=False)
    update = db.DateTimeProperty(verbose_name=_('Update'),auto_now=True)
    created = db.DateTimeProperty(verbose_name=_('Created'),auto_now_add=True)

class JLeagueTeam(db.Model):
    team_name = db.StringProperty(verbose_name=_('Team Name'),default='',indexed=False)
    team_short_name = db.StringProperty(verbose_name=_('Team Short Name'),default='',indexed=False)
    team_id = db.StringProperty(verbose_name=_('Team ID'),default='',indexed=False)
    j_class = db.StringProperty(verbose_name=_('J Class'),choices=('J1','J2'))
    update = db.DateTimeProperty(verbose_name=_('Update'),auto_now=True)
    created = db.DateTimeProperty(verbose_name=_('Created'),auto_now_add=True)

class JLeagueRank(db.Model):
    team = db.ReferenceProperty(JLeagueTeam)
    year = db.StringProperty(verbose_name=_('Year,Seson'),default='')
    rank = db.IntegerProperty(verbose_name=_('Rank'))
    point = db.IntegerProperty(verbose_name=_('Point'))
    game_count = db.IntegerProperty(verbose_name=_('Game Count'))
    win_count = db.IntegerProperty(verbose_name=_('Win Count'))
    draw_count = db.IntegerProperty(verbose_name=_('Draw Count'))
    lose_count = db.IntegerProperty(verbose_name=_('Lose Count'))
    goal_get = db.IntegerProperty(verbose_name=_('Goal Get'))
    goal_lost = db.IntegerProperty(verbose_name=_('Goal Lost'))
    goal_point = db.IntegerProperty(verbose_name=_('Goal Point'))
    update = db.DateTimeProperty(verbose_name=_('Update'),auto_now=True)
    created = db.DateTimeProperty(verbose_name=_('Created'),auto_now_add=True)

class JPlayerData(db.Model):
    display_page_flg = db.BooleanProperty(verbose_name=_('Display this page'),default=False)
    year = db.StringProperty(verbose_name=_('Year,Seson'),default='')
    player_type = db.StringProperty(verbose_name=_('Player Type'),choices=('Field','GK'),default='Field')
    title = db.StringProperty(verbose_name=_('Player Name'),default='')
    new_team = db.StringProperty(verbose_name=_('New Team Name'),default='')
    old_team = db.StringProperty(verbose_name=_('Old Team Name'),default='')
    trade_comment = db.StringProperty(verbose_name=_('Trade Comment'),default='')
    game_count = db.IntegerProperty(verbose_name=_(u'出場試合数'),default=0)
    goal_get = db.IntegerProperty(verbose_name=_(u'得点'),default=0)
    assist = db.IntegerProperty(verbose_name=_(u'アシスト'),default=0)
    shoot = db.IntegerProperty(verbose_name=_(u'シュート'),default=0)
    passn = db.IntegerProperty(verbose_name=_(u'パス'),default=0)
    dribble = db.IntegerProperty(verbose_name=_(u'ドリブル'),default=0)
    tackle = db.IntegerProperty(verbose_name=_(u'タックル'),default=0)
    clear = db.IntegerProperty(verbose_name=_(u'クリア'),default=0)
    intercept = db.IntegerProperty(verbose_name=_(u'インターセプト'),default=0)
    goal_lost = db.IntegerProperty(verbose_name=_(u'失点'),default=0)
    save_count = db.IntegerProperty(verbose_name=_(u'セーブ数'),default=0)
    save_ratio = db.FloatProperty(verbose_name=_(u'セーブ率'),default=0.0)
    catch = db.IntegerProperty(verbose_name=_(u'キャッチ'),default=0)
    punch = db.IntegerProperty(verbose_name=_(u'パンチ'),default=0)
    feed_throw = db.FloatProperty(verbose_name=_(u'フィード　スロー'),default=0.0)
    feed_kick = db.FloatProperty(verbose_name=_(u'フィード　キック'),default=0.0)
    update = db.DateTimeProperty(verbose_name=_('Update'),auto_now=True)
    created = db.DateTimeProperty(verbose_name=_('Created'),auto_now_add=True)
