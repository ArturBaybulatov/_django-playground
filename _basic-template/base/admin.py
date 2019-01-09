from django.contrib import admin



from . import models


admin.site.register(models.Product)
admin.site.register(models.Brand)
admin.site.register(models.Category)



## Enhanced admimn interface -----------------------------------
#
#from . import models, forms
#
#
#@admin.register(models.Product)
#class ProductAdmin(admin.ModelAdmin):
#    readonly_fields = ('pk',)
#    list_display = ('name','age_group','brand')
#    filter_horizontal = ('categories',)
#    search_fields = ('name','age_group','brand__name','categories__name')
#    list_filter = ('age_group',)
#
#
#@admin.register(models.Brand)
#class BrandAdmin(admin.ModelAdmin):
#    readonly_fields = ('pk',)
#    form = forms.BrandAdminForm
#
#    def save_model(self, request, brand, form, change):
#        brand.products = form.cleaned_data['products']
#        super().save_model(request, brand, form, change)
#
#
#@admin.register(models.Category)
#class CategoryAdmin(admin.ModelAdmin):
#    readonly_fields = ('pk',)
#    form = forms.CategoryAdminForm
#
#    def save_model(self, request, category, form, change):
#        category.products = form.cleaned_data['products']
#        super().save_model(request, category, form, change)



# import code; code.interact(local=dict(globals(), **locals()))
