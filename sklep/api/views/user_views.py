from django.contrib.auth.models import User
from users.models import UserProfile, Subscriber
from sklep.models import Address
from sklep.api.serializers import (UserSerializer, ProfileSerializer,
                                    AddressSerializer, SubscriberSerializer)
from sklep.api.pagination import CustomPagination

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter, BooleanFilter, ChoiceFilter, NumberFilter

class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (IsAuthenticatedOrReadOnly,)

class UserProfileListAPIView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = CustomPagination
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'
    # permission_classes = [IsOwnerOrReadOnly]
    permission_classes = (IsAuthenticatedOrReadOnly,)

class AddressDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)

class AddressFilters(FilterSet):
    user = CharFilter(field_name='user__username', lookup_expr='iexact')
    class Meta:
        model = Address
        fields = ['user__username']

class AddressListAPIView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AddressFilters

class SubscriberListAPIView(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)

class SubscriberDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)