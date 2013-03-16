from django.db import models
from django.contrib.localflavor.us.models import USStateField


class BaseModel(models.Model):

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Address(models.Model):

    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = USStateField()
    zipcode = models.CharField(max_length=100)

    class Meta:
        abstract = True
