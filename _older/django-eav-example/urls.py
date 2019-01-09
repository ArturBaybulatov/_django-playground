# from rest_framework import routers
from app import models, views
from django.conf import settings, urls
from django.contrib import admin


urlpatterns = [
  urls.url(r'^admin/', admin.site.urls),
  urls.url(r'^setup/', views.setup),
  urls.url(r'^advert-list/', views.AdvertList.as_view(), name='advert-list'),
  urls.url(r'^category-list/', views.CategoryList.as_view(), name='category-list'),
]




# router = routers.DefaultRouter()
# 
# router.register(r'categories', views.Category)
# router.register(r'adverts', views.Advert)
# # router.register(r'eav-attributes', views.EavAttribute) # Debug
# 
# urlpatterns += router.urls
# 
# 
# 
# # for heroku:
# 
# if settings.DEBUG:
#   urlpatterns += static(
#     settings.STATIC_URL,
#     document_root=settings.STATIC_ROOT
#   )
