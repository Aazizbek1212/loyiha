from django.contrib import admin

from apps.tour.models import Advantages, Category, Country, Destination, Gallery, Tour


admin.site.register(Tour)
admin.site.register(Destination)
admin.site.register(Country)
admin.site.register(Advantages)
admin.site.register(Category)
admin.site.register(Gallery)
