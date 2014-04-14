from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^events', views.show_events, name='events'),
    url(r'^peers', views.show_peers, name='peers'),
    url(r'^plan', views.plan, name='plan'),
)