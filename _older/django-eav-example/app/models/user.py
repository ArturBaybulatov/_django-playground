from django.db import models
import django.contrib.auth.models as auth_models
import mptt.models

from .location import Location


class User(auth_models.AbstractUser):
  TYPES = (
    ('person', 'Person'),
    ('company', 'Company'),
  )
  
  location = mptt.models.TreeForeignKey('Location', related_name='users', blank=True, null=True)
  type = models.CharField(max_length=20, choices=TYPES, blank=True, null=True)
