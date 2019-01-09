from django.contrib import admin

from . import models


admin.site.register(models.Product)
admin.site.register(models.Brand)
admin.site.register(models.Category)


# import code; code.interact(local=dict(globals(), **locals()))
