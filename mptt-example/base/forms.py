from django import forms
from django.contrib import admin

from . import models


class RegionAdminForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=models.Product.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple(verbose_name='products', is_stacked=False),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        region = self.instance

        if region.pk:
            self.fields['products'].initial = region.products.values_list('pk', flat=True)


class CategoryAdminForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=models.Product.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple(verbose_name='products', is_stacked=False),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category = self.instance

        if category.pk:
            self.fields['products'].initial = category.products.values_list('pk', flat=True)
