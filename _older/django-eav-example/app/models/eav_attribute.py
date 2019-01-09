from django.db import models
import eav.models
import mptt.models

from .category import Category


class EavAttribute(eav.models.Attribute):
  django_model = mptt.models.TreeForeignKey('Category', related_name='eav_attrs', blank=True, null=True)
  
  
  @classmethod
  def from_db(cls, db, field_names, values):
    # default implementation of from_db() (could be replaced
    # with super())
    
    if cls._deferred:
      instance = cls(**zip(field_names, values))
    else:
      instance = cls(*values)
    
    instance._state.adding = False
    instance._state.db = db
    
    # customization to store the original field values on the instance
    instance._loaded_values = dict(zip(field_names, values))
    
    return instance
  
  
  def save(self, *args, **kwargs):
    if not self._state.adding:
      if self.datatype != self._loaded_values['datatype']:
        raise ValueError(u"You cannot change the datatype of an attribute that is already in use.")
      
      if self.slug != self._loaded_values['slug']:
        raise ValueError(u"You cannot change the slug of an attribute that is already in use.")
    
    self.slug = '%s_____%s' % (self.django_model.slug, self.slug)
    super().save(*args, **kwargs)
