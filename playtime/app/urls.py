from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	# url(r'^admin/', include(admin.site.urls)),
	url(r'^events', views.show_events, name='events'),
	url(r'^new_events', views.events_plus, name='events-plus'), 	#fake response
    url(r'^peers', views.show_peers, name='peers'),
    url(r'^plan', views.plan, name='plan'),
)