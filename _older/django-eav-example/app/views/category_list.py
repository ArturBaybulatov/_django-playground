from django import shortcuts, http
from django.core import urlresolvers, exceptions
from django.views import generic

from app import models, forms

from pprint import pprint
import inspect
import itertools
import pydash as _; _.map = _.map_; _.filter = _.filter_



class CategoryList(generic.ListView):
  model = models.Category
  template_name = 'category-list.jinja'
  context_object_name = 'categories'


# import code; code.interact(local=dict(globals(), **locals()))
