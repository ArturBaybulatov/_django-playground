from django.contrib import admin

from . import models


admin.site.register(models.Categories)
admin.site.register(models.Customercustomerdemo)
admin.site.register(models.Customerdemographics)
admin.site.register(models.Customers)
admin.site.register(models.Employees)
admin.site.register(models.Employeeterritories)
admin.site.register(models.OrderDetails)
admin.site.register(models.Orders)
admin.site.register(models.Products)
admin.site.register(models.Region)
admin.site.register(models.Shippers)
admin.site.register(models.Suppliers)
admin.site.register(models.Territories)
admin.site.register(models.Usstates)


# import code; code.interact(local=dict(globals(), **locals()))
