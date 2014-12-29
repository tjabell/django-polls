from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite import views

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', views.index, name='index'),
                       url(r'^polls/', include('polls.urls',
                                               namespace="polls")),
                       url(r'^admin/', include(admin.site.urls)))
