from django.shortcuts import render, redirect
from playtime.app.models import Buddy, Event, Group
import json
from django.http import HttpResponse
import datetime

def index(request):
	# TODO: route to a different page if logged out?
	return redirect(show_events)

def show_events(request, buddy_id=None):
	# for a real site, these would be filtered by the current user
	current_user = Buddy.objects.get(id=13)
	events = Event.objects.all()
	buddies = Buddy.objects.all()
	groups = Group.objects.all()
	temp_vars = {
		"page_name": "events",
		"events": events,
		"groups": groups,
		"buddies": buddies,
		"current_user": current_user
	}
	buddy_id = request.GET.get('buddy_id')
	if buddy_id:
		temp_vars["filter_buddy"] = Buddy.objects.get(id=buddy_id)
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

def get_buddies_in_group(request, group_id):
	group = Group.objects.get(id=group_id)
	buddies = group.members.all()
	buddy_ids = []
	for buddy in buddies:
		buddy_ids.append(buddy.id)
	response_data = {"buddy_ids": buddy_ids}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def show_peers(request):
	# TODO: filter by group
	buddies = Buddy.objects.all()
	temp_vars = {
		"page_name": "buddies",
		"buddies": buddies
	}
	return render(request, 'peers.html', temp_vars)

#this is a helper
def date_from_string(date_str):
	m, d, y = date_str.split("/")
	return datetime.date(year=int(y), month=int(m), day=int(d))

def time_from_string(time_str):
	time, half = time_str.split(" ")
	h, m = time.split(":")
	if half == "PM":
		h = int(h)%12
	return datetime.time(hour=int(h), minute=int(m))

def plan(request):
	user = Buddy.objects.get(id=13) # stephen 

	if request.method == 'POST':
		data = request.POST
		title = data['title']
		description = data['description']
		location = data['location']
		start_time = time_from_string(data['start_time'])
		end_time = time_from_string(data['end_time'])
		date = date_from_string(data['date'])
		photo = data['photo']
		event = Event(title=title, description=description, location=location, start_time=start_time, end_time=end_time, date=date, photo=photo)
		event.created_by = user
		event.save()
		for group in data.getlist('groups[]'):
			Group.objects.get(id=int(group)).events.add(event)
		
		return redirect('events')

	temp_vars = {
		"page_name": "plan"
	}
	return render(request, 'plan.html', temp_vars)