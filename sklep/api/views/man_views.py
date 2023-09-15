
from sklep.models import (Manufacturer)
from sklep.api.serializers import (ManufacturerSerializer)
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter, BooleanFilter, ChoiceFilter, NumberFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from sklep.api.pagination import CustomPagination
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser

COUNTRIES = [
        ('usa', 'USA'),
        ('poland', 'Poland'),
        ('germany', 'Germany'),
        ('czech', 'Czech Republic')
    ]

class ManufacturerFilters(FilterSet):
    active = BooleanFilter(field_name="active")
    country = ChoiceFilter(field_name="country", choices=COUNTRIES)
    rating_gte = NumberFilter(field_name="rating_average", lookup_expr="gte")
    class Meta:
        model = Manufacturer
        fields = ['active', 'country', 'rating_average']

class ManufacturerListAPIView(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ['manufacturer__name', 'type']
    filterset_class = ManufacturerFilters

class ManufacturerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    lookup_field = 'slug'