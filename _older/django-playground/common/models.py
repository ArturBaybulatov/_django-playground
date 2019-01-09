from django.db import models


class Foo(models.Model):
    name = models.CharField(max_length=255, unique=True)
    text = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Foo'
        verbose_name_plural = 'Foos'
    
    def __str__(self):
        return self.name


class Bar(models.Model):
    name = models.CharField(max_length=255, unique=True)
    text = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Bar'
        verbose_name_plural = 'Bars'
    
    def __str__(self):
        return self.name
