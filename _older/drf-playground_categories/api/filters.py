import rest_framework_filters as filters
from . import models


class Category(filters.FilterSet):
  class Meta:
    model = models.Category
  
  slug = filters.AllLookupsFilter()
  name = filters.AllLookupsFilter()
  parent = filters.RelatedFilter('api.filters.Category') # self-references...
  children = filters.RelatedFilter('api.filters.Category')
  hidden = filters.AllLookupsFilter()
  foo = filters.AllLookupsFilter()
  adverts = filters.RelatedFilter('api.filters.Advert')


class Advert(filters.FilterSet):
  class Meta:
    model = models.Advert
  
  id = filters.AllLookupsFilter()
  name = filters.AllLookupsFilter()
  pictures = filters.RelatedFilter('api.filters.AdvertPicture')
  category = filters.RelatedFilter('api.filters.Category')


class AdvertPicture(filters.FilterSet):
  class Meta:
    model = models.AdvertPicture
  
  id = filters.AllLookupsFilter()
  # file = filters.AllLookupsFilter()
  advert = filters.RelatedFilter('api.filters.Advert')
