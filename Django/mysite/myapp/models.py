from django.db import models


class Friends(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_the_best = models.BooleanField(default=True)
