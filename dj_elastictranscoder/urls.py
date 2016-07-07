try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url  # Support for Django < 1.4

from . import views

urlpatterns = [
    url(r'^endpoint/$', views.endpoint),
]
