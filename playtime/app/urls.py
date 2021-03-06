from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	# url(r'^admin/', include(admin.site.urls)),
	url(r'^events', views.show_events, name='events'),
	url(r'^events/(?P<buddy_id>[0-9])/$', views.show_events),
	url(r'^get_events_for_group/(?P<group_id>[0-9])/$', views.get_events_for_group),
	url(r'^get_events_for_buddy/(?P<buddy_id>[0-9])/$', views.get_events_for_buddy),
	url(r'^get_buddies_in_group/(?P<group_id>[0-9])/$', views.get_buddies_in_group),
	url(r'^join_event/(?P<child_id>[0-9])/(?P<event_id>[0-9])/$', views.join_event),
    url(r'^peers', views.show_peers, name='peers'),
    url(r'^plan', views.plan, name='plan'),
)