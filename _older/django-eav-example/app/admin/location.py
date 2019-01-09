from django.contrib import admin
import mptt.admin

from app import models, forms


class Location(mptt.admin.MPTTModelAdmin):
  readonly_fields = ('pk', 'lft', 'rght', 'tree_id', 'level')
  form = forms.Location


admin.site.register(models.Location, Location)
