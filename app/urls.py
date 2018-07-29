from django.conf.urls import include, url
from . import views 
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.inicio),
    url(r'^home/reports/$', views.home, name='home'),
    url(r'^home/reports/autoreporte$', views.autoreporte, name='autoreporte'),
    url(r'^home/reports/kolb$', views.kolb, name='kolb'),
    url(r'^home/reports/edward$', views.edward, name='edward'),
    url(r'^home/reports/tap$', views.tap, name='tap'),
    url(r'^home/reports/sigae$', views.sigae, name='sigae'),
    ]