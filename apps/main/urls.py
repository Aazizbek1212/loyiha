from django.urls import path
from apps.main.views import home_view, tour_view

urlpatterns = [
    path('', home_view, name='home'),
    path('tours/', tour_view, name='tours'),
]
