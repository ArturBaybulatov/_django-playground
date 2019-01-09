from rest_framework import serializers
import eav.models # eav.models.Entity

from app import models


# class Category(serializers.HyperlinkedModelSerializer):
#   class Meta:
#     model = models.Category
#     fields = ('id', 'name', 'parent', 'children', 'adverts', 'eav_attrs')
# 
# 
# class Advert(serializers.HyperlinkedModelSerializer):
#   # TODO: problem with serializing EAV's enums
#   
#   class Meta:
#     model = models.Advert
#     fields = ('id', 'name', 'category', 'eav')
#   
#   # eav = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#   eav = serializers.SerializerMethodField()
#   
#   def get_eav(self, obj):
#     return obj.eav.get_values_dict()
# 
# 
# class EavAttribute(serializers.HyperlinkedModelSerializer):
#   class Meta:
#     model = models.EavAttribute
#     fields = ('id', 'name', 'slug', 'django_model')
