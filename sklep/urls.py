from django.urls import path

from . import views

app_name="sklep"
urlpatterns = [
    path("other", views.other_django_view, name="other"),
    path(r'vue/', views.VueView.as_view(), name='vue_app'),
    path(r'vue/<path:path>', views.VueView.as_view(), name='vue_app_with_path'),

    # path('', views.index, name='index'),
]
