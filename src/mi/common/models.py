from django.db import models
from django.contrib.localflavor.us.models import USStateField


class BaseModel(models.Model):

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):

    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zipcode = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True
