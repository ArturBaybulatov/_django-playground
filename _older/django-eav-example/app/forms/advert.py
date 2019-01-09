from django import forms
import eav.forms

from app import models

import pydash as _


# class Advert(forms.ModelForm):
#   # class Meta:
#   #   # model = models.Advert
#   #   readonly_fields = ('id',)
#   
#   saved_by = forms.ModelMultipleChoiceField(queryset=models.User.objects.none(), required=False)
#   
#   def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self.fields['saved_by'].queryset = self.instance.saved_by.all() # TODO: Advert creation error


class Advert(eav.forms.BaseDynamicEntityForm):
  class Meta:
    model = models.Advert
    exclude = ()
  
  
  def _build_dynamic_fields(self, *args, **kwargs):
    super()._build_dynamic_fields(*args, **kwargs)
    
    _.each(self.entity.get_all_attribute_slugs(), lambda k:
      self.fields.pop(k) if k.split('_____')[0] != self.entity.model.category.slug else None
    )


# import code; code.interact(local=dict(globals(), **locals()))
