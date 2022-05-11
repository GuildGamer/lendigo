from django.db import models
from django.contrib.postgres.fields import ArrayField

class Item(models.Model):
    # base item
    id = models.BigIntegerField(primary_key=True)
    by = models.CharField(max_length=256, null=True, blank=True)
    kids = ArrayField(models.IntegerField(), null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    time = models.BigIntegerField(null=True, blank=True)
    type = models.CharField(max_length=256)
    deleted = models.BooleanField(null=True, blank=True)
    dead = models.BooleanField(null=True, blank=True)
    
    title = models.CharField(max_length=256, null=True, blank=True)
    descendants = models.IntegerField(null=True, blank=True)
    url = models.URLField(max_length=512, null=True, blank=True)
    text = models.CharField(max_length=10000, null=True, blank=True)
    parts = ArrayField(models.IntegerField(), null=True, blank=True)

