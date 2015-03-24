from django.db import models

# Create your models here.
class web(models.Model):
	website = models.CharField(max_length=100)
	email = models.TextField(default="")
	data = models.TextField(default="")
	
	def __str__(self):
		return self.website
