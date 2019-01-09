from django.conf import urls
from django.contrib import admin
from rest_framework import routers

from . import viewsets


router = routers.DefaultRouter()

router.register(r'notes', viewsets.Note)
router.register(r'categories', viewsets.Category)

urlpatterns = [
    urls.url(r'^', urls.include(router.urls)),
    urls.url(r'^auth/', urls.include('rest_framework.urls')),
    urls.url(r'^admin/', urls.include(admin.site.urls)),
]
