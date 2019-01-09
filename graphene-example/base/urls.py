from django.conf import urls
from django.contrib import admin
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView

from . import views


urlpatterns = [
    urls.url(r'^$', views.HomeView.as_view(), name='home'),
    urls.url(r'^admin/', urls.include(admin.site.urls)),
    urls.url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]
