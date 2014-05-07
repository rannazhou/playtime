from django.shortcuts import render, redirect
from playtime.app.models import Buddy, Event, Group
import json
from django.http import HttpResponse

def index(request):
	# TODO: route to a different page if logged out?
	return redirect(show_events)

def show_events(request):
	# for a real site, these would be filtered by the current user
	events = Event.objects.all()
	groups = Group.objects.all()
	temp_vars = {
		"page_name": "events",
		"events": events,
		"groups": groups
	}
	return render(request, 'events.html', temp_vars)

# called via AJAX to add user to event
def join_event(request, child_id, event_id):
	child = Buddy.objects.get(id=child_id)
	event = Event.objects.get(id=event_id)
	event.attendees.add(child)

def get_events_for_group(request, group_id):
	group = Group.objects.get(id=group_id)
	events = group.events.all()
	event_ids = []
	for event in events:
		event_ids.append(event.id)
	response_data = {"event_ids": event_ids}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def get_events_for_buddy(request, buddy_id):
	buddy = Buddy.objects.get(id=buddy_id)
	events = buddy.events_attending.all()
	event_ids = []
	for event in events:
		event_ids.append(event.id)
	response_data = {"event_ids": event_ids}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def events_plus(request):
	temp_vars = {
		"page_name": "events"
	}
	return render(request, 'events-plus.html', temp_vars)

def show_peers(request):
	# TODO: filter by group
	buddies = Buddy.objects.all()
	temp_vars = {
		"page_name": "buddies",
		"buddies": buddies
	}
	return render(request, 'peers.html', temp_vars)

def plan(request):
	temp_vars = {
		"page_name": "plan"
	}
	return render(request, 'plan.html', temp_vars)