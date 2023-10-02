from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, UserEditForm
from django.contrib.auth import login as auth_login
from users.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import UpdateView

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            #create an attached user profile
            # profile = UserProfile.objects.create(user=user, profile_img=form.cleaned_data.get("profile_img"))
            profile = UserProfile.objects.create(user=user, bio=form.cleaned_data.get("bio"))
            profile.save()
            #log the created user in
            auth_login(request, user)
            return redirect('sklep:home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.django-html', {'form': form})

@login_required()
def edit_view(request):
    # initial_user = request.user
    user = request.user
    initial_data = {
        'email' : user.email,
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'bio': user.profile.bio
    }
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES,
                            initial = initial_data,
                            instance = user)
        if form.is_valid():
            user = form.save()
            profile = UserProfile.objects.get(user=request.user)
            profile.bio = form.cleaned_data.get("bio")
            profile.save()
            # user.save()
            return redirect("sklep:home")
            # return redirect('accounts:edit')
    else:
        form = UserEditForm(initial=initial_data, instance = user)
        # form = UserEditForm(instance=initial_user)
    return render(request, 'accounts/account.django-html', {'form': form})