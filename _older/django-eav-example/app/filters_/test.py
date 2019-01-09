# import eav.models
import rest_framework_filters as filters
from api import models


class Category(filters.FilterSet):
  class Meta:
    model = models.Category
  
  id = filters.AllLookupsFilter()
  name = filters.AllLookupsFilter()
  parent = filters.RelatedFilter('api.filters.Category') # self-references...
  children = filters.RelatedFilter('api.filters.Category')
  adverts = filters.RelatedFilter('api.filters.Advert')
  eav_attrs = filters.RelatedFilter('api.filters.EavAttribute')


class Advert(filters.FilterSet):
  class Meta:
    model = models.Advert
  
  id = filters.AllLookupsFilter()
  name = filters.AllLookupsFilter()
  category = filters.RelatedFilter('api.filters.Category')


class EavAttribute(filters.FilterSet):
  class Meta:
    model = models.EavAttribute
  
  id = filters.AllLookupsFilter()
  name = filters.AllLookupsFilter()
  slug = filters.AllLookupsFilter()
  django_model = filters.RelatedFilter('api.filters.Category')
