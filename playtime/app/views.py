from django.shortcuts import render, redirect
from playtime.app.models import Buddy, Event

def index(request):
	# TODO: route to a different page if logged out?
	return redirect(show_events)

def show_events(request):
	events = Event.objects.all()
	temp_vars = {
		"page_name": "events",
		"events": events
	}
	return render(request, 'events.html', temp_vars)

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