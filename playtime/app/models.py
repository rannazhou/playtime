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
	created_by = models.ForeignKey('Buddy')

class Group(models.Model):
	name = models.CharField(max_length=50)

class Membership(models.Model):
	child = models.ForeignKey('Buddy')
	group = models.ForeignKey('Group')