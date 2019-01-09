from django import forms

from app import models


class Location(forms.ModelForm):
  users = forms.ModelMultipleChoiceField(queryset=models.User.objects.none(), required=False)
  
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.fields['users'].queryset = models.User.objects.filter(
      location__lft__gte = self.instance.lft,
      location__rght__lte = self.instance.rght,
    )
