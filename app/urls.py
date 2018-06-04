from django.conf.urls import include, url
from . import views 
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.inicio),
    url(r'^home/reports/$', views.home, name='home'),
    url(r'^home/reports/autoreporte$', views.autoreporte, name='autoreporte'),
    ]