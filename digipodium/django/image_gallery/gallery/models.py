
from django.db.models import *


# Create your models here.

class Category(Model):
    name= CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Image(Model):
    image= ImageField(upload_to='images/')
    title= CharField(max_length=30)
    category= ForeignKey("Category", on_delete=CASCADE)