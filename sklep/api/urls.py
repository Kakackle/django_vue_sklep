from django.urls import include, path
from .views import ProductDetailAPIView, ProductListAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name="api_product_list"),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name="api_product_detail")
]