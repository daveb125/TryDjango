from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.TextField()
    surname = models.TextField()
    email = models.TextField()
    password = models.TextField()
    active = models.TextField()