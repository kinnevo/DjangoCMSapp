from django.db import models

# Create your models here.
from django.db import models
from django.utils import timesince

class Activity(models.Model):
    activity_id = models.IntegerField(default=0)
    activity = models.CharField(max_length=80)
    description = models.TextField()
    category = models.CharField(max_length=80)
    image = models.URLField(default="")
    image_file = models.FileField(upload_to='uploads/', default="")


    def write_activity(self):
        self.save()

    def __str__(self):
        return self.activity