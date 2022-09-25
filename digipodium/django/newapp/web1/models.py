from django.db import models
from django.db.models import *

# Create your models here.

class Movies(models.Model):
    title= CharField(max_length=50)
    year= IntegerField()
    rating= FloatField()
    def __str__(self) -> str:
        return self.title
class Show(models.Model):
    title= CharField(max_length=60)
    year= IntegerField()
    rating= FloatField()
    seasons= IntegerField()
    created_at= DateTimeField(auto_now=True)