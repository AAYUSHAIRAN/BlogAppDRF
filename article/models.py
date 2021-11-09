from enum import unique
from django.db import models

# Create your models here.
class Article(models.Model):
    heading = models.CharField(max_length=200, unique = True, blank=False)
    content = models.CharField(max_length=200, blank=False)