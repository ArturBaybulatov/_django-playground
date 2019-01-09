from django.db import models
import eav
import mptt.models

from .category import Category
from .user import User


class Advert(models.Model):
  name = models.CharField(max_length=50)
  category = mptt.models.TreeForeignKey('Category', related_name='adverts', blank=True, null=True)
  user = models.ForeignKey('User', related_name='adverts', blank=True, null=True)
  
  def __str__(self):
    return self.name


eav.register(Advert)
