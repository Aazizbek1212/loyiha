from django.shortcuts import render

from apps.tour.models import Advantages, Country, Destination, Tour



def home_view(request):
    advantages = Advantages.objects.all()
    destinations = Destination.objects.all()[:4]
    destinations6 = Destination.objects.order_by('-created_at')[:1]
    destinations1 = Destination.objects.filter(continent='Asia')[:4]
    destinations2 = Destination.objects.filter(continent='Europe')[:4]
    destinations3 = Destination.objects.filter(continent='Africa')
    destinations4 = Destination.objects.filter(continent='South America')
    destinations5 = Destination.objects.filter(continent='North America')
    tour1 = Tour.objects.filter(countries=1)
    tour2 = Tour.objects.exclude(countries=1)[:4]
    country = Country.objects.all()[:12]
    return render(request, 'index.html', {'advantages': advantages, 'destinations1':destinations1,
                                          'destinations2':destinations2,
                                          'destinations3':destinations3,
                                          'destinations4':destinations4,
                                          'destinations5':destinations5,
                                          'destinations':destinations,
                                          'destinations6':destinations6,
                                          'tour1':tour1,
                                          'tour2':tour2,
                                          'country':country})


def tour_view(request, pk):
    tour = Tour.objects.all()
    tours1 = Tour.objects.filter(continent='Asia')[:4]
    tours2 = Tour.objects.filter(continent='Europe')[:4]
    tours3 = Tour.objects.filter(continent='Africa')
    tours4 = Tour.objects.filter(continent='South America')
    tours5 = Tour.objects.filter(continent='North America')
    return render(request, 'tours.html', {'tour':tour,
                                          'tours1':tours1,
                                          'tours2':tours2,
                                          'tours3':tours3,
                                          'tours4':tours4,
                                          'tours5':tours5})