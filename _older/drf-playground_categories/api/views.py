from django.views import generic
from django.core import urlresolvers
from django import http
#from django.shortcuts import render
from rest_framework import viewsets as rest_viewsets
from . import models, forms, serializers, filters


from pprint import pprint
import pydash as _; _.map = _.map_; _.filter = _.filter_
import itertools
import inspect



# class CategoryList(generic.ListView):
#   model = models.Category
#   template_name = '3/index.jinja'
#   # template_name = 'category-list.jinja'
#   context_object_name = 'categories'
#   queryset = models.Category.objects.filter(level=0).exclude(hidden=True)
# 
# 
# class CategoryUpdate(generic.edit.UpdateView):
#   model = models.Category
#   fields = '__all__'
#   template_name = 'category-update.jinja'
#   context_object_name = 'category'
#   success_url = urlresolvers.reverse_lazy('category-list')
#   
#   # def get_context_data(self, **kwargs):
#   #   context = super(CategoryUpdate, self).get_context_data(**kwargs)
#   #   context['adverts'] = context['category'].adverts.all()
#   #   return context
# 
# 
# class CategoryDelete(generic.edit.DeleteView):
#   model = models.Category
#   fields = '__all__'
#   template_name = 'category-delete.jinja'
#   context_object_name = 'category'
#   success_url = urlresolvers.reverse_lazy('category-list')








class AdvertList(generic.ListView):
  model = models.Advert
  template_name = '3/index.jinja'
  # template_name = 'advert-list.jinja'
  context_object_name = 'adverts'
  
  
  def get_context_data(self, **kwargs):
    slug = self.kwargs.get('slug') # TODO: Need query param sanitation
    context = super(AdvertList, self).get_context_data(**kwargs)
    
    if slug != 'all':
      context['category'] = models.Category.objects.get(slug=slug)
    
    context['categories'] = models.Category.objects.filter(level=1).exclude(hidden=True)
    context['form'] = forms.CategoryTree
    
    return context
  
  
  def get_queryset(self, **kwargs):
    slug = self.kwargs.get('slug') # TODO: Need query param sanitation
    
    if slug != 'all':
      category = models.Category.objects.get(slug=slug)
      adverts = models.Advert.objects.filter(category__lft__gte=category.lft, category__rght__lte=category.rght)
    else:
      slug = self.request.GET.get('category') or 'all' # TODO: Need query param sanitation
      
      if slug != 'all':
        category = models.Category.objects.get(slug=slug)
        adverts = models.Advert.objects.filter(category__lft__gte=category.lft, category__rght__lte=category.rght)
      else:
        adverts = models.Advert.objects.all()
    
    return adverts



class AdvertUpdate(generic.edit.UpdateView):
  model = models.Advert
  fields = '__all__'
  template_name = 'advert-update.jinja'
  context_object_name = 'advert'
  success_url = urlresolvers.reverse_lazy('advert-list')



class AdvertDelete(generic.edit.DeleteView):
  model = models.Advert
  fields = '__all__'
  template_name = 'advert-delete.jinja'
  context_object_name = 'advert'
  success_url = urlresolvers.reverse_lazy('advert-list')






def test(req):
  # # x = req.GET.get('foo')
  # 
  # import code; code.interact(local=dict(globals(), **locals()))
  
  return http.HttpResponse('blah')













#---------------------------------------------------------





class CategoryAPI(rest_viewsets.ModelViewSet):
  queryset = models.Category.objects.all()
  serializer_class = serializers.Category
  filter_class = filters.Category


class AdvertAPI(rest_viewsets.ModelViewSet):
  queryset = models.Advert.objects.all()
  serializer_class = serializers.Advert
  filter_class = filters.Advert


class AdvertPictureAPI(rest_viewsets.ModelViewSet):
  queryset = models.AdvertPicture.objects.all()
  serializer_class = serializers.AdvertPicture
  filter_class = filters.AdvertPicture









#------------------------------------------------------------



def setup(req):
  models.setup()
  return http.HttpResponse('ok')









# import code; code.interact(local=dict(globals(), **locals()))
