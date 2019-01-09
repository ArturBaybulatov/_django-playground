from django.conf import urls

from . import views


urlpatterns = [
    urls.url(r'^file-upload$', views.FileUploadView.as_view(), name='file-upload'),
]
