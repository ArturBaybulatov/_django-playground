from django.contrib import auth
from rest_framework import serializers

from app import models

import pydash as _; _.map = _.map_; _.filter = _.filter_


class Category(serializers.ModelSerializer):
  class Meta:
    model = models.Category
    fields = _.map(models.Category._meta.get_fields(), lambda f: f.name)


class Location(serializers.ModelSerializer):
  class Meta:
    model = models.Location
    fields = _.map(models.Location._meta.get_fields(), lambda f: f.name)


class User(serializers.ModelSerializer):
  class Meta:
    model = models.User
    
    fields = (
      'adverts',
      'date_joined',
      'email',
      'first_name',
      'groups',
      'id',
      'is_active',
      'is_authenticated',
      'is_staff',
      'is_superuser',
      'last_login',
      'last_name',
      'location',
      'type',
      'user_permissions',
      'username',
    )


class Advert(serializers.ModelSerializer):
  class Meta:
    model = models.Advert
    
    # fields = _.map(models.Advert._meta.get_fields(), lambda f: f.name)
    
    fields = (
      'category',
      'name',
      'user',
      # 'eav...',
    )
  
  user = User()


class AnonymousUser(serializers.ModelSerializer):
  class Meta:
    model = models.User
    
    fields = (
      'get_username',
      'groups',
      'id',
      'is_active',
      'is_anonymous',
      'is_authenticated',
      'is_staff',
      'user_permissions',
      'username',
    )


# import code; code.interact(local=dict(globals(), **locals()))
