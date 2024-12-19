from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    assigned_users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
