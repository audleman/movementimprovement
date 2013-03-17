from django.contrib import admin

from classes.models import ATMClass
from classes.models import Location


class ATMClassAdmin(admin.ModelAdmin):
    list_display = ('location', 'date', 'time')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ATMClass, ATMClassAdmin)
admin.site.register(Location, LocationAdmin)
