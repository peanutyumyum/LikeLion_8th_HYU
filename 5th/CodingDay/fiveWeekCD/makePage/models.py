from django.db import models

# Create your models here.

class youTubeChannel(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20)
    preference = models.IntegerField()
    live = models.BooleanField()
    subscribers = models.IntegerField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()

