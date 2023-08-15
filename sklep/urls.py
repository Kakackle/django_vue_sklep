from django.urls import path

from . import views

urlpatterns = [
    path(r'vue/', views.VueView.as_view(), name='vue_app'),
    path(r'vue/<path:path>', views.VueView.as_view(), name='vue_app_with_path'),
    # path('', views.index, name='index'),
]
