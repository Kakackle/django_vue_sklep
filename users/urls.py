from .models import UserProfile
from django.urls import path
from django.contrib.auth.models import User
from . import views

app_name = "users"
urlpatterns = [
    path("<str:username>", views.user_view, name="user"),
]