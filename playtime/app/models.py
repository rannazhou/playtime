from django.db import models

# Create your models here.
class Buddy(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	parent1 = models.CharField(max_length=30)
	parent2 = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='uploads/')

class Event(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	location = models.CharField(max_length=100)
	created_by = models.ForeignKey(Buddy, related_name='events_created')
	description = models.TextField()
	photo = models.ImageField(upload_to='events/')
	attendees = models.ManyToManyField(Buddy, related_name='events_attending')

class Group(models.Model):
	name = models.CharField(max_length=50)
	members = models.ManyToManyField(Buddy)
	events = models.ManyToManyField(Event)