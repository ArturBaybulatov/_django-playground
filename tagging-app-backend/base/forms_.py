from django import forms
from django.contrib import admin

from . import models


#class TagAdminForm(forms.ModelForm):
#    notes = forms.ModelMultipleChoiceField(
#        queryset=models.Note.objects.all(),
#        widget=admin.widgets.FilteredSelectMultiple(verbose_name='notes', is_stacked=False),
#        required=False,
#    )
#
#    synonyms = forms.ModelMultipleChoiceField(
#        queryset=models.Synonym.objects.all(),
#        widget=admin.widgets.FilteredSelectMultiple(verbose_name='synonyms', is_stacked=False),
#        required=False,
#    )
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        tag = self.instance
#
#        if tag.pk:
#            self.fields['notes'].initial = tag.notes.values_list('pk', flat=True)
#            self.fields['synonyms'].initial = tag.synonyms.values_list('pk', flat=True)
