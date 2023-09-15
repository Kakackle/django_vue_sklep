from sklep.models import Product, ProductImage, EffectType
from sklep.api.serializers import (ProductSerializer, ProductImageSerializer,
                                   EffectTypeSerializer)
from sklep.api.pagination import CustomPagination

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter, BooleanFilter, ChoiceFilter, NumberFilter

from django.http import JsonResponse

class ProductFavouriteAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,) 

    def patch(self, request, *args, **kwargs):
        print('update request data:', self.request.data)
        return self.partial_update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        user = self.request.user
        user_profile = user.profile

        product_slug = self.kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)

        if product not in user_profile.favourite_products.all():
            user_profile.favourite_products.add(product)
            user_profile.favourite_count +=1
            user_profile.save()
        else:
            user_profile.favourite_products.remove(product)
            user_profile.favourite_count -=1
            user_profile.save()

        favourite_products = list(user_profile.favourite_products.all()
                                  .values_list('slug', flat=True))
        
        # print('fav products: ', favourite_products)
        return JsonResponse({'liked_by': favourite_products, 
                             'message': 'liked_by changed'},status=200)
    
class ProductFilters(FilterSet):
    manufacturer = CharFilter(field_name='manufacturer__slug', lookup_expr='contains')
    type = CharFilter(field_name='type', lookup_expr='contains')
    price_lte = NumberFilter(field_name='price', lookup_expr="lte")
    price_gte = NumberFilter(field_name='price', lookup_expr="gte")
    discount_gte = NumberFilter(field_name="discount", lookup_expr="gte")
    rating_gte = NumberFilter(field_name="rating_average", lookup_expr="gte")
    favourited_by = CharFilter(field_name='favourited_by__user__username', lookup_expr='contains')
    class Meta:
        model = Product
        fields = ['manufacturer__slug', 'type', 'price', 'discount', 'rating_average',
                  'favourited_by__user__username']

class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ['manufacturer__name', 'type']
    filterset_class = ProductFilters
    
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    lookup_field = 'slug'
    # permission_classes = [IsOwnerOrReadOnly]

class ImageFilters(FilterSet):
    product = CharFilter(field_name='product__slug', lookup_expr='exact')

    class Meta:
        model = ProductImage
        fields = ['product__slug',]

class ProductImageListAPIView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ImageFilters

class ProductImageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    lookup_field = 'slug'

class EffectTypeListAPIView(generics.ListCreateAPIView):
    queryset = EffectType.objects.all()
    serializer_class = EffectTypeSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class EffectTypeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EffectType.objects.all()
    serializer_class = EffectTypeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    lookup_field = 'slug'