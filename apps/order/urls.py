from django.urls import path
from .views import  order_view, review_create

urlpatterns = [
    path('tour/<int:pk>/review', review_create, name='review_create'),
    path('order/', order_view, name='order'),
]
