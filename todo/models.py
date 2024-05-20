from django.db import models
from django.contrib.auth.models import User

TASKS_STATUS = (
	(1, "To-do"),
	(2, "Done")
)

class LocationChoices(models.TextChoices):
    LONDON = 'London,UK', 'London'
    BERLIN = 'Berlin,DE', 'Berlin'
    PARIS = 'Paris,FR', 'Paris',
    DUBAI = 'Dubai,AE', 'Dubai',
    STOCKHOLM = 'Stockholm,SE', 'Stockholm'
    WROCLAW = 'Wroclaw,PL', 'Wrocław'
    
class Task(models.Model):	
	user=models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
	note=models.CharField(verbose_name="Note",
						max_length=100,
						null=False,
						blank=False)
	status=models.IntegerField(verbose_name="Status",
						null=False,
						blank=False,
						choices=TASKS_STATUS,
						default=1)
	location = models.CharField(verbose_name="Location", choices = LocationChoices.choices,
						max_length=20,
						null=True,
						blank=True)
    
	latitude = models.FloatField(verbose_name="Latitude",
						null=True,
						blank=True)
    
	longitude = models.FloatField(verbose_name="Longitude",
						null=True,
						blank=True)
	weather	= models.CharField(verbose_name="Weather",
                        max_length=20,
                        null=True,
                        blank=True)
	temp	= models.FloatField(verbose_name="Temperature",
                        null=True,
                        blank=True)
    
	class Meta:
		verbose_name = "Task"
		verbose_name_plural = "Tasks"
		ordering = ['status']
	    
	def __str__(self):
		return self.note
    