from django.urls import path

from . import views

app_name="newsletter"
urlpatterns = [
    # path('new_subscriber/', views.new_subscriber, name='new_subscriber'),
    path('confirm/', views.confirm, name="newsletter_confirm"),
    path('unsubscribe/', views.unsubscribe, name="newsletter_unsubscribe"),
]