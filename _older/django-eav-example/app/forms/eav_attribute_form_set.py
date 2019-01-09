from django import forms

from app import models


class EavAttributeFormSetExtras(forms.BaseInlineFormSet):
  pass


EavAttributeFormSet = forms.inlineformset_factory(
  models.Category,
  models.EavAttribute,
  exclude = (),
  extra = 1,
  formset = EavAttributeFormSetExtras,
)
