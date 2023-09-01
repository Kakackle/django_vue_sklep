from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

# TODO: aktualizacja jak beda inne modele
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(null=True, blank=True, max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
