from django.contrib import admin
from playtime.app.models import Buddy, Event, Group

class GroupAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

class BuddyAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name']

class EventAdmin(admin.ModelAdmin):
	list_display = ['id', 'title']


admin.site.register(Buddy, BuddyAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Group, GroupAdmin)