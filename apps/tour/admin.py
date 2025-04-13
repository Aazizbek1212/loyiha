from django.contrib import admin

from apps.tour.models import Advantages, Country, Destination, Tour


admin.site.register(Tour)
admin.site.register(Destination)
admin.site.register(Country)
admin.site.register(Advantages)
