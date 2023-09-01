from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.crypto import get_random_string
# Create your models here.

def upload_to_profile(instance, filename):
    random_str = get_random_string(length=6)
    return 'images/profiles/{random}-{filename}'.format(
        filename=filename, random=random_str
    )

# TODO: aktualizacja jak beda inne modele
class UserProfile(models.Model):
    USER_TYPES = (
        ('client', 'client user'),
        ('admin', 'admin user'),
        ('manufacturer', 'manufacturer user')
    )
    type = models.CharField(max_length=30, choices=USER_TYPES)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(null=True, blank=True, max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True,
                                      default="../static/img/placeholder_avatar.png",
                                      upload_to=upload_to_profile)
    review_count = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username
