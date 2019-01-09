from django import shortcuts, http
from django.core import urlresolvers, exceptions
from django.views import generic
from rest_framework import renderers

from app import models, forms, serializers

from pprint import pprint
import inspect
import itertools
import pydash as _; _.map = _.map_; _.filter = _.filter_



class AdvertList(generic.ListView):
  model = models.Advert
  template_name = 'advert-list.jinja'
  context_object_name = 'adverts'
  
  
  def get_queryset(self, *args, **kwargs):
    # https://docs.djangoproject.com/en/dev/ref/request-response/#querydict-objects
    
    category_id = self.request.GET.get('category_id')
    
    if category_id: return models.Advert.objects.filter(category__pk=category_id)
    else: return models.Advert.objects.all()
  
  
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    data = context['data'] = {}
    
    
    category_id = self.request.GET.get('category_id')
    
    
    if self.request.user.is_authenticated():
      # ser = serializers.User(self.request.user, context={'request_user': self.request.user})
      ser = serializers.User(self.request.user)
      data['user'] = renderers.JSONRenderer().render(ser.data).decode()
    else:
      ser = serializers.AnonymousUser(self.request.user)
      data['user'] = renderers.JSONRenderer().render(ser.data).decode()
    
    # ser = serializers.Category(models.Category.objects.all())
    # data['category'] = renderers.JSONRenderer().render(ser.data).decode()
    
    ser = serializers.Category(models.Category.objects.all(), many=True)
    data['categories'] = renderers.JSONRenderer().render(ser.data).decode()
    
    ser = serializers.Location(models.Location.objects.all(), many=True)
    data['locations'] = renderers.JSONRenderer().render(ser.data).decode()
    
    
    if category_id: adverts = models.Advert.objects.filter(category__pk=category_id)
    else: adverts = models.Advert.objects.all()
    
    ser = serializers.Advert(adverts, many=True)
    data['adverts'] = renderers.JSONRenderer().render(ser.data).decode()
    
    
    return context


# import code; code.interact(local=dict(globals(), **locals()))
