from rest_framework import serializers
from . import models


class Category(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Category
    fields = ('pk', 'name', 'parent', 'children', 'hidden', 'foo', 'adverts')


class Advert(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Advert
    fields = ('pk', 'name', 'pictures', 'category')


class AdvertPicture(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.AdvertPicture
    # fields = ('pk', 'file', 'advert')
    fields = ('pk', 'advert')
