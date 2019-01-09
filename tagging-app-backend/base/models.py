from django.db import models
import mptt.models


class Note(models.Model):
    name = models.CharField(max_length=255)
    tags = mptt.models.TreeManyToManyField('Tag', related_name='notes', blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Tag(mptt.models.MPTTModel):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True)
    parent = mptt.models.TreeForeignKey('self', related_name='children', null=True, blank=True, db_index=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name','type')
        ordering = ('name',)

    class MPTTMeta:
        order_insertion_by = ('type','name')

    def __str__(self):
        return self.name


class Synonym(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True)
    master = mptt.models.TreeForeignKey('Tag', related_name='synonyms', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name','type')
        ordering = ('name',)

    def __str__(self):
        return self.name
