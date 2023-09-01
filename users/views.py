from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def user_view(request, username):
    user = UserProfile.objects.get(user__username=username)
    context = {
        'user': user 
    }
    return render(request, "users/user.django-html", context)