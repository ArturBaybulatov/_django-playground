from django.conf import urls
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r'categories', views.CategoryAPI)
# router.register(r'adverts', views.AdvertAPI)
# router.register(r'advert-pictures', views.AdvertPictureAPI)
# urlpatterns = router.urls



urlpatterns = [
  urls.url(r'^category/(?P<slug>[\w-]+)/$', views.AdvertList.as_view(), name='advert-list'),
  
  urls.url(r'^adverts/(?P<pk>\d+)/update/$', views.AdvertUpdate.as_view(), name='advert-update'),
  urls.url(r'^adverts/(?P<pk>\d+)/delete/$', views.AdvertDelete.as_view(), name='advert-delete'),
  
  
  urls.url(r'^setup/$', views.setup),
  
  urls.url(r'^test/$', views.test),
]
