from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
  url(r'^api/', include('api.urls')),
  url(r'^admin/', admin.site.urls),
]

# # for heroku:
# 
# if settings.DEBUG:
#   urlpatterns += static(
#     settings.STATIC_URL,
#     document_root=settings.STATIC_ROOT
#   )
