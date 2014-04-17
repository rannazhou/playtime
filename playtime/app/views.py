from django.shortcuts import render, redirect


def index(request):
	# TODO: route to a different page if logged out?
	return redirect(show_events)

def show_events(request):
	temp_vars = {
		"page_name": "events"
	}
	return render(request, 'events.html', temp_vars)

def events_plus(request):
	temp_vars = {
		"page_name": "events"
	}
	return render(request, 'events-plus.html', temp_vars)

def show_peers(request):
	temp_vars = {
		"page_name": "peers"
	}
	return render(request, 'peers.html', temp_vars)

def plan(request):
	temp_vars = {
		"page_name": "plan"
	}
	return render(request, 'plan.html', temp_vars)