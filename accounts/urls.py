from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="accounts"
urlpatterns = [
    #user
    path("signup", views.signup_view, name="signup"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.django-html'), name='login'),
    path("edit", views.edit_view, name="edit"),
    # path("delete", views.delete_view, name="delete"),
    # path("password", views.change_password, name="password")
]