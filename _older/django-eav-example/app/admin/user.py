from django.contrib import admin

from app import models, forms


class User(admin.ModelAdmin):
  readonly_fields = ('pk',)
  form = forms.User


admin.site.register(models.User, User)
