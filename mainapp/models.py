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
