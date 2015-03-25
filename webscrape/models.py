from django.db import models

# Create your models here.
class web(models.Model):
	website = models.CharField(max_length=100)
	emails = models.TextField(default="")
	links = models.TextField(default="")
	
	def __str__(self):
		return self.website
