
from django.forms import ModelForm
from wanderful.models import Traveler
from wanderful.models import TravelList
from wanderful.models import Location


__author__ = 'Jeffng'


class TravelerForm(ModelForm):
    class Meta:
        model = Traveler


class TravelListForm(ModelForm):
    class Meta:
        model = TravelList


class LocationForm(ModelForm):
    class Meta:
        model = Location


