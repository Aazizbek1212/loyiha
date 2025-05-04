from django.urls import path
from apps.main.views import DavlatSearchView, ShaharSearchView, TourSearchView, country_view, destinatio_tour_view, destination_view, destinations_view, gallery_view, home_view, tour_detail_view, tour_view

urlpatterns = [
    path('', home_view, name='home'),
    path('tours/', tour_view, name='tours'),
    path('destinations/', destinations_view, name='destination'),
    path('countrys/', country_view, name='countrys'),
    path('tourdetail/<int:pk>/', tour_detail_view, name='tour_detail'),
    path('country_destination/<int:pk>/', destination_view, name='country_destination'),
    path('destination_tour/<int:pk>/', destinatio_tour_view, name='destination_tour'),
    path('gallery/', gallery_view, name='gallery'),
    path('DavlatSearch/', DavlatSearchView.as_view(), name='country_search'),  # DavlatSearchView
    path('ShaharSearch/', ShaharSearchView.as_view(), name='destination_search'),  # ShaharSearchView
    path('TourSearch/', TourSearchView.as_view(), name='tour_search'),  # TourSearchView
]
