from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Estadisticas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'', include('app.urls')),

)
