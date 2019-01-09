from django.contrib import admin
import mptt.admin
from . import models, forms


class AdvertInline(admin.TabularInline):
  model = models.Advert
  extra = 0

class Category(mptt.admin.MPTTModelAdmin):
  readonly_fields = ['pk', 'lft', 'rght', 'tree_id', 'level']
  inlines = [AdvertInline]

admin.site.register(models.Category, Category)



class Advert(admin.ModelAdmin):
  readonly_fields = ['pk']

admin.site.register(models.Advert, Advert)



class AdvertPicture(admin.ModelAdmin):
  readonly_fields = ['pk']

admin.site.register(models.AdvertPicture, AdvertPicture)
