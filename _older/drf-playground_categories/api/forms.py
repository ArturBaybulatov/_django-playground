from django import forms
import mptt.forms
from . import models

import pydash as _; _.map = _.map_; _.filter = _.filter_
from pprint import pprint
import itertools
import inspect


# class AttributeFormSetForm(forms.ModelForm):
#   # def save(self, *args, **kwargs):
#   #   pass
#   
#   def clean(self):
#     print('\n>>>>>>>>>>>> forms: AttributeFormSetForm "clean" attempt <<<<<<<<<<<<\n')
#     # cleaned_data = super(ArticleFormSetForm, self).clean()
#     # cleaned_data['name'] = cleaned_data['name'].upper() # experim.
#     # return cleaned_data


# class AttributeFormSetExtras(forms.BaseInlineFormSet):
#   pass
# 
# AttributeFormSet = forms.inlineformset_factory(
#   models.Category,
#   models.Attribute,
#   exclude = (),
#   extra = 0,
#   formset = AttributeFormSetExtras,
# )



class CategoryTree(forms.Form):
  category = mptt.forms.TreeNodeChoiceField(queryset=models.Category.objects.all())
