from django.conf.urls import include, url
from . import views 
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home),
    #url(r'^logout/$', views.logout,{'next_page':'accounts:login'}),
    ]