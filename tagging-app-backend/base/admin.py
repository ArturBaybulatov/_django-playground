from django.contrib import admin
import mptt.admin

from . import models


#@admin.register(models.Note)
#class NoteAdmin(admin.ModelAdmin):
#    readonly_fields = ('pk',)
#    filter_horizontal = ('tags',)
#
#
#@admin.register(models.Tag)
#class TagAdmin(mptt.admin.MPTTModelAdmin):
#    readonly_fields = ('pk',)
#    list_display = ('name','type')
#    form = forms.TagAdminForm
#
#    def save_model(self, request, tag, form, change):
#        super().save_model(request, tag, form, change)
#        tag.notes = form.cleaned_data['notes']
#        tag.synonyms = form.cleaned_data['synonyms']
#
#
#@admin.register(models.Synonym)
#class SynonymAdmin(admin.ModelAdmin):
#    readonly_fields = ('pk',)
#    list_display = ('name','type','master')

admin.site.register(models.Note)
admin.site.register(models.Tag, mptt.admin.MPTTModelAdmin)
admin.site.register(models.Synonym)


# import code; code.interact(local=dict(globals(), **locals()))
