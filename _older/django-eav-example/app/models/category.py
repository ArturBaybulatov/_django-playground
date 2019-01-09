from django.db import models
import mptt.models


class Category(mptt.models.MPTTModel):
  name = models.CharField(max_length=50)
  parent = mptt.models.TreeForeignKey('self', blank=True, null=True, related_name='children', db_index=True)
  
  class Meta:
    verbose_name_plural = 'categories'
  
  def __str__(self):
    return self.name
