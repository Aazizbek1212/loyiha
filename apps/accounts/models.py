from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.main.models import BaseModel


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    yosh = models.IntegerField(null=True, blank=True)
    telefon_raqami = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=150, blank=True, null=True)  # Usernamedan nusxa
    email = models.EmailField(blank=True, null=True)      # Emaildan nusxa

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, username=instance.username, email=instance.email)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    profile = instance.userprofile
    profile.username = instance.username
    profile.email = instance.email
    profile.save()
