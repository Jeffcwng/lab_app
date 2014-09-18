from django.contrib import admin

# Register your models here.
from wanderful.models import User, UserList, Location

admin.site.register(User)
admin.site.register(UserList)
admin.site.register(Location)
