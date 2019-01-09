from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    brand = models.ForeignKey('Brand', related_name='products', blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='products', blank=True) # These are `null=True` anyway

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    luxury = models.BooleanField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
