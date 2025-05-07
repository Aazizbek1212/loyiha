from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.main.models import BaseModel
from apps.tour.models import Tour


class Review(BaseModel):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)
    

class Order(BaseModel):
    name = models.CharField(max_length=200)
    phone_number = PhoneNumberField(max_length=20)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    date = models.DateField()
    person = models.PositiveIntegerField(default=1)
    child = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.tour.name} ({self.date})"