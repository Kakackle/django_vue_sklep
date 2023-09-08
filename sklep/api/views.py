from django.shortcuts import get_object_or_404
from sklep.models import (Product, Manufacturer, User)
from users.models import UserProfile
from sklep.api.serializers import (ProductSerializer, ManufacturerSerializer,
                                   UserSerializer, ProfileSerializer)
from .permissions import IsOwnerOrReadOnly
from.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics
from rest_framework.response import Response

from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import FormParser, MultiPartParser

from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter

class UserProfileListAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = CustomPagination
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'
    # permission_classes = [IsOwnerOrReadOnly]

class ManufacturerListAPIView(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    pagination_class = CustomPagination
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ManufacturerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'slug'

    # def get_object(self):
    #     obj = get_object_or_404(self.get_queryset(), slug=self.kwargs["slug"])
    #     self.check_object_permissions(self.request, obj)
    #     return obj

class ProductFilters(FilterSet):
    manufacturer = CharFilter(field_name='manufacturer__slug', lookup_expr='contains')
    type = CharFilter(field_name='type', lookup_expr='contains')

    class Meta:
        model = Product
        fields = ['manufacturer__slug', 'type']

class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ['manufacturer__name', 'type']
    filterset_class = ProductFilters
    
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    # permission_classes = [IsOwnerOrReadOnly]

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'token': csrf_token})