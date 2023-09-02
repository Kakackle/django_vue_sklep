from django.urls import path

from . import views

app_name="sklep"
urlpatterns = [
    path("other", views.other_django_view, name="other"),
    path(r'', views.vue_view, name='home'),
    path(r'<path:path>', views.vue_view, name='home_path'),

    # path('', views.index, name='index'),
]
