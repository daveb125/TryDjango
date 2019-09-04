from django.db import models

# Create your models here.

class Profile(models.Model):
    title = models.CharField(max_length = 120,null=True)
    name = models.TextField(null=True)
    surname = models.TextField(null=True)
    email = models.TextField(blank=True,null=False)
    password = models.TextField()
    active = models.TextField(default='y')
    price = models.DecimalField(decimal_places=2,max_digits=10000,default=0)