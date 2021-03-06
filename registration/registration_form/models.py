from cProfile import label
from logging import PlaceHolder
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=130)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(max_length=500, default="")

    def __str__(self):
        return self.name