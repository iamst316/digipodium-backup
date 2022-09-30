from ast import For
from unicodedata import name
from unittest.util import _MAX_LENGTH
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
    def __str__(self) -> str:
        return self.title

class Student(models.Model):
    name= CharField(max_length=35)
    klass= IntegerField(verbose_name='Class')
    rollno= IntegerField()

    def __str__(self) -> str:
        return self.name


class Report(models.Model):
    english= IntegerField()
    maths= IntegerField()
    science=IntegerField()
    hindi= IntegerField()
    socsci=IntegerField()
    student= ForeignKey('Student',on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return f'Report of {self.student.name}'

class Weather(models.Model):
    temp= DecimalField(verbose_name="Temp(C)",max_digits=4, decimal_places=2)
    wind_speed= DecimalField(max_digits=4, decimal_places=2)
    humidity= DecimalField(max_digits=4, decimal_places=2)
    date= DateField(auto_now_add=True)

    def __str__(self):
        return self.temp


class Artist(models.Model):
    name= CharField(max_length=30)
    grammys= IntegerField()

    def __str__(self) -> str:
        return self.name

class Song(models.Model):
    name= CharField(max_length=50)
    artist= ForeignKey('Artist', on_delete= DO_NOTHING)
    release_date= DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.name