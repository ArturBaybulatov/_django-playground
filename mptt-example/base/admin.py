from django.contrib import admin
import mptt.admin

from . import models, forms


#admin.site.register(models.Product)
#admin.site.register(models.Region)
#admin.site.register(models.Category)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)
    list_display = ('name','region')
    filter_horizontal = ('categories',)
    search_fields = ('name','region__name','categories__name')


@admin.register(models.Region)
class RegionAdmin(mptt.admin.MPTTModelAdmin):
    readonly_fields = ('pk',)
    form = forms.RegionAdminForm

    def save_model(self, request, region, form, change):
        region.products = form.cleaned_data['products']
        super().save_model(request, region, form, change)


@admin.register(models.Category)
class CategoryAdmin(mptt.admin.MPTTModelAdmin):
    readonly_fields = ('pk',)
    form = forms.CategoryAdminForm

    def save_model(self, request, category, form, change):
        category.products = form.cleaned_data['products']
        super().save_model(request, category, form, change)
