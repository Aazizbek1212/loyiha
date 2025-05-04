from django.db import models

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