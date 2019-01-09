from django.contrib.auth import get_user_model
from django.db import models


class Note(models.Model):
    name = models.CharField(max_length=255)
    private = models.BooleanField()
    share_count = models.PositiveIntegerField()
    category = models.ForeignKey('Category', related_name='notes', blank=True, null=True)
    author = models.ForeignKey(get_user_model(), related_name='notes', blank=True, null=True)

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
