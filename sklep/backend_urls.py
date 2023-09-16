from django.urls import path

from . import views

app_name="backend"
urlpatterns = [
    path("products/create", views.new_product_view, name="product_create"),
    path("products/<slug:product_slug>/edit", views.edit_product_view, name="product_edit"),
    path("products/<slug:product_slug>/delete", views.delete_product_view, name="product_delete"),
    path("products/<slug:product_slug>/<slug:image_slug>/delete", views.delete_image_view, name="delete_image"),
    
    path("manufacturers/create",
        views.manufacturer_create.as_view(template_name="sklep/manufacturer_create.django-html"),
        name="manufacturer_create"),
    path("manufacturers/<slug:slug>/update",
        views.manufacturer_update.as_view(template_name="sklep/manufacturer_create.django-html"),
        name="manufacturer_update"),

    path("effect_type/create",
        views.effect_type_create.as_view(template_name="sklep/effect_type_create.django-html"),
        name="effect_type_create"),
    path("effect_type/<slug:slug>/update",
        views.effect_type_update.as_view(template_name="sklep/effect_type_create.django-html"),
        name="effect_type_update"),

    path("shipping/create",
        views.shipping_create.as_view(template_name="sklep/shipping_create.django-html"),
        name="shipping_create"),
    path("shipping/<slug:slug>/update",
        views.shipping_update.as_view(template_name="sklep/shipping_create.django-html"),
        name="shipping_update"),

    path("cart/create",
        views.cart_create.as_view(template_name="sklep/cart_create.django-html"),
        name="cart_create"),
]