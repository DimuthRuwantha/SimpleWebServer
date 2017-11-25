from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.password
