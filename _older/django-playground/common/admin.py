from django.contrib import admin

from .models import Foo, Bar


class FooAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)

admin.site.register(Foo, FooAdmin)


class BarAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)

admin.site.register(Bar, BarAdmin)
