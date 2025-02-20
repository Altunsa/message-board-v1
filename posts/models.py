from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)