from django.urls import path

from . import views

app_name="sklep"
urlpatterns = [
    path("other", views.other_django_view, name="other"),
    path("products/create", views.new_product_view, name="product_create"),
    path("products/<slug:product_slug>/edit", views.edit_product_view, name="product_edit"),
    path(r'', views.vue_view, name='home'),
    path(r'<path:path>', views.vue_view, name='home_path'),

    # path('', views.index, name='index'),
]
