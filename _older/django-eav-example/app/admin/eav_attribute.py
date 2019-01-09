from django.contrib import admin
import eav.admin

from app import models, forms


class EavAttribute(eav.admin.ModelAdmin):
  readonly_fields = ('pk',)
  form = forms.EavAttribute


admin.site.register(models.EavAttribute, EavAttribute)
