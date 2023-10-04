from django.contrib.auth.models import User
from users.models import UserProfile
from newsletter.models import Subscriber
from sklep.models import Address
from sklep.api.serializers import (UserSerializer, ProfileSerializer,
                                    AddressSerializer, SubscriberSerializer)
from sklep.api.pagination import CustomPagination

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter, BooleanFilter, ChoiceFilter, NumberFilter

# mailing
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse

# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

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

# @method_decorator(csrf_exempt, name='dispatch')
class SubscriberListAPIView(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            print('errors:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        email = self.request.data.get('email')
        conf_num = random_digits()
        name = self.request.data.get('name')
        frequency = self.request.data.get('frequency')
        sub = Subscriber(email=email, conf_num=conf_num, name=name, frequency=frequency)
        sub.save()
        print("from_email: ", settings.FROM_EMAIL)
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(self.request.build_absolute_uri(reverse('newsletter:newsletter_confirm')),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        # serializer.save()

class SubscriberDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)