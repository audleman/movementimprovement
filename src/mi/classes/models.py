from django.db import models
from common.models import BaseModel
from common.models import Address


class ATMClass(BaseModel):
    """ One class that I taught """
    location = models.ForeignKey('classes.Location')
    series = models.ForeignKey('classes.ATMSeries')
    date = models.DateField()
    time = models.TimeField()


class ATMSeries(BaseModel):
    """ A grouping of classes """
    name = models.CharField(max_length=255)
    location = models.ForeignKey('classes.Location')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)


class Location(BaseModel, Address):
    """ Studio, apartment, wherever I teach a class """
    name = models.CharField(max_length=255)


class Attendance(BaseModel):

    atm_class = models.ForeignKey('classes.ATMClass')
    person = models.ForeignKey('people.Person')
    payment = models.OneToOneField('payments.Payment')
