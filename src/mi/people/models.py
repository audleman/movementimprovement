from django.db import models
from common.models import BaseModel, Address
from django.contrib.localflavor.us.models import PhoneNumberField


class Person(BaseModel, Address):

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True)
