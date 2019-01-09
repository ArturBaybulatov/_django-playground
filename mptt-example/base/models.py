from django.db import models
import mptt.models


class Product(models.Model):
    name = models.CharField(max_length=255)
    region = mptt.models.TreeForeignKey('Region', related_name='products', null=True, blank=True)
    categories = mptt.models.TreeManyToManyField('Category', related_name='products', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Region(mptt.models.MPTTModel):
    name = models.CharField(max_length=255)
    parent = mptt.models.TreeForeignKey('self', related_name='children', null=True, blank=True, db_index=True)

    class Meta:
        ordering = ('name',)

    class MPTTMeta:
        order_insertion_by = ('name',)

    def __str__(self):
        return self.name


class Category(mptt.models.MPTTModel):
    name = models.CharField(max_length=255)
    parent = mptt.models.TreeForeignKey('self', related_name='children', null=True, blank=True, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        order_insertion_by = ('name',)

    def __str__(self):
        return self.name
