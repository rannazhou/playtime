from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	# url(r'^admin/', include(admin.site.urls)),
	url(r'^events', views.show_events, name='events'),
	url(r'^get_events_for_group/(?P<group_id>[0-9])/$', views.get_events_for_group),
	url(r'^join_event/(?P<child_id>[0-9])/(?P<event_id>[0-9])/$', views.join_event),
	url(r'^new_events', views.events_plus, name='events-plus'), 	#fake response
    url(r'^peers', views.show_peers, name='peers'),
    url(r'^plan', views.plan, name='plan'),
)