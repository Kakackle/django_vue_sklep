from django.urls import include, path
from .views import (ProductDetailAPIView, ProductListAPIView, ManufacturerDetailAPIView,
                    ManufacturerListAPIView, UserProfileListAPIView, UserProfileDetailAPIView,
                    get_csrf_token)

app_name="api"
urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name="api_product_list"),
    path('products/<slug:slug>/', ProductDetailAPIView.as_view(), name="api_product_detail"),
    path('manufacturers/', ManufacturerListAPIView.as_view(), name="api_man_list"),
    path('manufacturers/<slug:slug>/', ManufacturerDetailAPIView.as_view(), name="api_man_detail"),
    path('profiles/', UserProfileListAPIView.as_view(), name="api_profile_list"),
    path('profiles/<slug:slug>/', UserProfileDetailAPIView.as_view(), name="api_profile_detail"),
    path('get_token', get_csrf_token, name="get_token"),
]