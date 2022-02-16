from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	bio = models.TextField()
	
	def __str__(self):
		return self.first_name
