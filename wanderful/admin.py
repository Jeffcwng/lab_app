from django.contrib import admin

# Register your models here.
from wanderful.models import *

admin.site.register(Traveler)
admin.site.register(TravelList)
admin.site.register(Location)
