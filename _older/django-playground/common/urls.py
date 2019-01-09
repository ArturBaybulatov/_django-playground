from django.conf.urls import url
from django.views.generic import TemplateView

from .views import (
    RedirectedView,
    HelloView,
    HomeView,
    LoginView,
    LogoutView,
)

app_name = 'common'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    
    url(r'^hello/$', HelloView.as_view(), name='hello'),
    url(r'^redirected/$', RedirectedView.as_view(), name='redirected'),
    
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
