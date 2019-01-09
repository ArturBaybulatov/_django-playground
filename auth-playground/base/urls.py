from .lib.baybulatov_django_util import djutil
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView
import urllib

from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^protected/$', views.ProtectedView.as_view(), name='protected'),
    url(r'^message/$', TemplateView.as_view(template_name='base/message.html'), name='message'),

    url(r'^accounts/', include([
        url(r'^register/$', views.RegisterView.as_view(), name='register'),

        url(r'^password_change/$', auth_views.PasswordChangeView.as_view(
            success_url=djutil.reverse_with_query('message', {'text': 'Password successfully changed'}),
        ), name='password_change'),

        url(r'^password_reset/$', auth_views.PasswordResetView.as_view(
            success_url=djutil.reverse_with_query('message', {'text': (
                'You should receive an email with instructions for setting your password '
                'if an account exists with the email you entered'
            )}),
        ), name='password_reset'),

        url(
            r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',

            auth_views.PasswordResetConfirmView.as_view(
                success_url=djutil.reverse_with_query('message', {'text': 'Password successfully reset'}),
                post_reset_login=True,
            ),

            name='password_reset_confirm',
        ),
    ])),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


# import code; code.interact(local=dict(globals(), **locals()))
