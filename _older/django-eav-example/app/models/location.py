from django.db import models
import mptt.models


class Location(mptt.models.MPTTModel):
  TYPES = (
    ('region', 'регион'),
    ('town', 'город'),
    ('district', 'район'),
    ('subway', 'метро'),
  )
  
  name = models.CharField(max_length=50)
  parent = mptt.models.TreeForeignKey('self', blank=True, null=True, related_name='children', db_index=True)
  type = models.CharField(max_length=20, choices=TYPES, blank=True, null=True)
  
  
  def __str__(self):
    return self.name
