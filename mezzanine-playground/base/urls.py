from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.i18n import set_language

from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings


admin.autodiscover()

urlpatterns = i18n_patterns(
    url("^admin/", include(admin.site.urls)),
)

if settings.USE_MODELTRANSLATION:
    urlpatterns += [
        url('^i18n/$', set_language, name='set_language'),
    ]

urlpatterns += [
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    #url("^$", mezzanine.pages.views.page, {"slug": "/"}, name="home"),
    #url("^$", mezzanine.blog.views.blog_post_list, name="home"),

    url("^", include("mezzanine.urls")),
    #("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls")),
]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
