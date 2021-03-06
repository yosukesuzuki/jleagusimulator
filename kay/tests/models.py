# -*- coding: utf-8 -*-

"""
Models for Kay tests.

:Copyright: (c) 2009 Accense Technology, Inc. All rights reserved.
:license: BSD, see LICENSE for more details.
"""

from google.appengine.ext import db

from kay.utils.forms import ValidationError
from kay.utils.forms.modelform import ModelForm

class MaxLengthValidator(object):

  def __init__(self, length):
    self.length = length

  def __call__(self, val):
    if len(val) > self.length:
      raise ValidationError("Too long")
    return True
  

class TestModel(db.Model):
  number = db.IntegerProperty(required=True)
  data_field = db.StringProperty(required=True,
                                 validator=MaxLengthValidator(20))
  is_active = db.BooleanProperty(required=True)
  string_list_field = db.StringListProperty(required=True)

class TestModel2(db.Model):
  number = db.IntegerProperty(required=True)
  data_field = db.StringProperty(required=True,
                                 validator=MaxLengthValidator(20))
  is_active = db.BooleanProperty(required=True)
  string_list_field = db.StringListProperty(required=True)


class TestModelForm(ModelForm):
  csrf_protected = False
  class Meta():
    model = TestModel
  def __init__(self, instance=None, initial=None):
    super(TestModelForm, self).__init__(instance, initial)
    self.string_list_field.min_size = 1


class JsonTestModel(db.Model):
  s = db.StringProperty()
  i = db.IntegerProperty()
  b = db.BooleanProperty()
  l = db.StringListProperty()
  r = db.ReferenceProperty()

class ModelFormTestModel(db.Model):
  s_name = db.StringProperty()
  zip_code = db.StringProperty()
  addr = db.StringProperty()

class ModelFormTestForm(ModelForm):
  csrf_protected = False
  class Meta:
    model = ModelFormTestModel
    fields = ('s_name')

class ValidationTestModel(db.Model):
  slist = db.StringListProperty()

class ValidationTestForm(ModelForm):
  csrf_protected = False
  class Meta:
    model = ValidationTestModel
  def context_validate(self, data):
    raise ValidationError("Error!")
