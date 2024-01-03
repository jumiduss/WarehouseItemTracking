from django.contrib import admin
from stockmanager.models import Location,StockedItem

admin.site.register(Location)
admin.site.register(StockedItem)