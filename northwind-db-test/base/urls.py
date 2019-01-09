from django.conf import urls
from django.contrib import admin


urlpatterns = [
    urls.url(r'^admin/', urls.include(admin.site.urls)),
]
