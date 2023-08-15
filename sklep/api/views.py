from sklep.models import Product, Profile
from sklep.api.serializers import ProductSerializer, ProfileSerializer
from rest_framework import generics

class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer