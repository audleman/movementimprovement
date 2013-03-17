import backbone
from backbone.views import BackboneAPIView
from classes.models import ATMClass, Location


class ATMClassView(BackboneAPIView):
    model = ATMClass
    display_fields = ('location', 'date', 'time')


class LocationView(BackboneAPIView):
    model = Location
    display_fields = ('name',)

backbone.site.register(ATMClassView)
backbone.site.register(LocationView)
