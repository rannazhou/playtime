from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'^events', views.show_events, name='events'),
	url(r'^events-plus', views.events_plus, name='events-plus'), 	#fake response
    url(r'^peers', views.show_peers, name='peers'),
    url(r'^plan', views.plan, name='plan'),
)