from django import forms

from app import models



class Category(forms.ModelForm):
  adverts = forms.ModelMultipleChoiceField(queryset=models.Advert.objects.none(), required=False)
  
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.fields['adverts'].queryset = models.Advert.objects.filter(
      category__lft__gte = self.instance.lft,
      category__rght__lte = self.instance.rght,
    )
  
  
  # def save(self, *args, **kwargs):
  #   orig_commit = kwargs['commit']
  #   kwargs['commit'] = False
  #   inst = super().save(*args, **kwargs)
  #   inst.name = self.cleaned_data['name'].upper()
  #   
  #   if orig_commit:
  #     inst.save()
  #   
  #   return inst


#import code; code.interact(local=dict(globals(), **locals()))
