from django.contrib import admin
import eav.admin

from app import models, forms


class Advert(eav.admin.BaseEntityAdmin):
  readonly_fields = ('pk',)
  form = forms.Advert


admin.site.register(models.Advert, Advert)
