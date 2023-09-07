from .models import UserProfile
from django.urls import path
from django.contrib.auth.models import User
from . import views

app_name = "users"
urlpatterns = [
    path("<slug:slug>/edit",
        views.profile_update.as_view(template_name="users/profile_update.django-html"),
        name="user"),
]