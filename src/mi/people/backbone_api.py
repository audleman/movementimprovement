import backbone
from backbone.views import BackboneAPIView
from people.models import Person


class PersonAPIView(BackboneAPIView):
    model = Person
    display_fields = ('first_name', 'last_name', 'email', 'phone')


backbone.site.register(PersonAPIView)
