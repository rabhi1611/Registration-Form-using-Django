from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField()
    branch = models.CharField(max_length=30)
    year = models.CharField(max_length=1)
    query = models.TextField(blank=True)

    def __str__(self):
        return self.name