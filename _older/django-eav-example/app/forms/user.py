from django import forms

from app import models


class User(forms.ModelForm):
  adverts = forms.ModelMultipleChoiceField(queryset=models.Advert.objects.none(), required=False)
  
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.fields['adverts'].queryset = self.instance.adverts.all()
