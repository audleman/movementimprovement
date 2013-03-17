from django.db import models
from common.models import BaseModel, Address
from django.contrib.localflavor.us.models import PhoneNumberField


class Person(BaseModel, Address):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
