from django.conf import urls
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from . import viewsets


router = routers.DefaultRouter()

router.register(r'notes', viewsets.Note)
router.register(r'tags', viewsets.Tag)
router.register(r'synonyms', viewsets.Synonym)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', urls.include(router.urls)),
    path('auth/', urls.include('rest_framework.urls')),
]
