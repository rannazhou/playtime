from django.shortcuts import render


def index(request):
	# TODO: route to a different page if logged out?
	return render(request, 'events.html')

def show_events(request):
	return render(request, 'events.html')

def show_peers(request):
	return render(request, 'peers.html')

def plan(request):
	return render(request, 'plan.html')