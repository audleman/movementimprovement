from datetime import date
from django.db import models
from common.models import BaseModel

PAYMENT_TYPES = (
    ('cash', 'Cash'),
    ('check', 'Check'),
    ('cc', 'Credit Card'),
    ('paypal', 'Paypal'),
    ('comp', 'Comp'))


class Payment(BaseModel):

    person = models.ForeignKey('people.Person')
    amount = models.DecimalField()
    date = models.DateField(default=date.today)
    type = models.CharField(max_length=20,
                choices=PAYMENT_TYPES)
