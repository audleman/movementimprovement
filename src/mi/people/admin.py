from django.contrib import admin

from people.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')

admin.site.register(Person, PersonAdmin)
