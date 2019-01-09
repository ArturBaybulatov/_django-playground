from django.contrib import admin
import mptt.admin

from app import models, forms


class EavAttributeInline(admin.TabularInline):
  model = models.EavAttribute
  formset = forms.EavAttributeFormSet
  extra = 0


class Category(mptt.admin.MPTTModelAdmin):
  readonly_fields = ('pk', 'lft', 'rght', 'tree_id', 'level')
  form = forms.Category
  inlines = (EavAttributeInline,)


admin.site.register(models.Category, Category)
