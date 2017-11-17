from __future__ import unicode_literals
from django.db import models

# Create your models here.

class timelapseParams(models.Model):
    total_images = models.IntegerField()
    length = models.IntegerField()
    interval = models.IntegerField()
    shutter_speed = models.IntegerField()
    direction = models.CharField(max_length=1)

    class JSONAPIMeta:
        resource_name = "tlParams"
