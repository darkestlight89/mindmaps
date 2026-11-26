from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):

    def __str__(self):
        return self.username

class Node(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    connections = models.ManyToManyField("self", blank=True, symmetrical=False)

    def clean(self):
        if ((self.title == "" or self.self.title == None) 
            and (self.body == "" or self.self.body == None) and 
            (self.image == "" or self.self.image == None)):
                raise ValidationError("At least one field must not be empty")

        if self.connections.filter(id=self.id).exists():
            raise ValidationError("Node cannot be connected to itself")
