from django.db import models

# Create your models here.

class Users(models.Model):
	email = models.CharField(primary_key=True, max_length = 100)
	firstName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	password = models.CharField(max_length = 20)