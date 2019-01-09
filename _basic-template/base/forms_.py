## Enhanced admimn interface -----------------------------------
#
#from django import forms
#from django.contrib import admin
#
#from . import models
#
#
#class BrandAdminForm(forms.ModelForm):
#    products = forms.ModelMultipleChoiceField(
#        queryset=models.Product.objects.all(),
#        widget=admin.widgets.FilteredSelectMultiple(verbose_name='products', is_stacked=False),
#        required=False,
#    )
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        brand = self.instance
#
#        if brand.pk:
#            self.fields['products'].initial = brand.products.values_list('pk', flat=True)
#
#
#class CategoryAdminForm(forms.ModelForm):
#    products = forms.ModelMultipleChoiceField(
#        queryset=models.Product.objects.all(),
#        widget=admin.widgets.FilteredSelectMultiple(verbose_name='products', is_stacked=False),
#        required=False,
#    )
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        category = self.instance
#
#        if category.pk:
#            self.fields['products'].initial = category.products.values_list('pk', flat=True)
