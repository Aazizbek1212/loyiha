from django.urls import path
from .views import review_create

urlpatterns = [
    path('tour/<int:pk>/review', review_create, name='review_create'),
]
