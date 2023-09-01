from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import UserProfile
from django.core.exceptions import ValidationError

def validate_username_blacklist(value):
    blacklist = ['admin', 'signup', 'logout', 'login', 'password', 'edit', 'delete']
    if value in blacklist:
        raise ValidationError('Please pick a different username')

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=255, validators=[validate_username_blacklist]) 
    email = forms.CharField(max_length=255, required=True,
                            widget=forms.EmailInput())
    first_name = forms.CharField(max_length=32, required=True, help_text="First name")
    last_name = forms.CharField(max_length=64, required=True, help_text="Last name")
    # profile_img = forms.ImageField(required=False)
    bio = forms.CharField(max_length=1000, widget=forms.Textarea(), required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
        # , 'profile_img'

class UserEditForm(forms.ModelForm):
    # profile_img = forms.ImageField(required=False)
    bio = forms.CharField(max_length=500, widget=forms.Textarea)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'bio')
        # , 'profile_img'