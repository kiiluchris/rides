from django.conf.urls import include, url

from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^coords/$', coords, name='coords'),
]
