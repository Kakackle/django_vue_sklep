from sklep.models import Order, OrderItem, Shipping, Address, Discount
from sklep.api.serializers import (OrderSerializer, OrderItemSerializer,
                                    ShippingSerializer, DiscountSerializer)
from sklep.api.pagination import CustomPagination

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal

from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter, BooleanFilter, ChoiceFilter, NumberFilter

from django.http import JsonResponse

from django.utils.text import slugify

class OrderFilters(FilterSet):
    user = CharFilter(field_name='user__username', lookup_expr='iexact')
    status = CharFilter(field_name='status', lookup_expr='iexact')

    class Meta:
        model = Order
        fields = ['user__username', 'status']

class OrderListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilters

    # tworzenie zamowien z mozliwoscia tworzenia jednoczesnie nowych adresow,
    # czyszczeniem koszyka, aplikowania 
    def post(self, request, *args, **kwargs):
        print('order post rquest data: ', request.data)
        return self.create(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            print('serializer errors: ', serializer.errors)
            return Response({"message": "not created"}, status=404)

    def perform_create(self, serializer):
        user = self.request.user
        # cart = Cart.objects.get(user = user)
        cart = user.cart
        # jesli w froncie zaznaczone ze nowy adres
        if self.request.data.get('new_address'):
            country = self.request.data.get('country')
            street = self.request.data.get('street')
            street_number = self.request.data.get('street_number')
            zipcode = self.request.data.get('zipcode')

            new_address = Address.objects.create(country=country, street=street,
                                                 street_number=street_number, zipcode=zipcode,
                                                 user=user)
            address = new_address
        else:
            # w przeciwnym razie oczekujesz adresu podanego z frontu
            address_pk = self.request.data.get('address')
            address = Address.objects.get(pk = address_pk)

        # discount przychodzi w wartosci liczbowej aktualnie
        discount = Decimal(self.request.data.get('discount'))
        sum_cost = Decimal(cart.sum_cost) * (1 - discount)
        shipping_slug = slugify(str(self.request.data.get('shipping_method')).lower())
        shipping_method = Shipping.objects.get(slug = shipping_slug)
        shipping_cost = shipping_method.price
        if (sum_cost < 250):
            sum_cost += shipping_cost
        sum_items = cart.sum_items
        status = 'progress'
        user = user
        
        order = Order.objects.create(user=user, address=address, status=status,
                discount=discount, sum_cost = sum_cost, sum_items=sum_items, shipping_method=shipping_method,
                shipping_cost=shipping_cost)

        # items = []
        for item in cart.items.all():
            order_item = OrderItem.objects.create(product=item.product,
                                              quantity=item.quantity,
                                              order=order)
            item.product.save()
            item.product.manufacturer.save()
        
        return JsonResponse({'data': serializer.data, 
                        'message': 'added to orders'},status=200)


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class OrderItemListAPIView(generics.ListCreateAPIView):
    # queryset = CartItem.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        order_pk = self.kwargs.get('pk')
        order = Order.objects.get(pk=order_pk)
        return OrderItem.objects.filter(order=order)
        # return super().get_queryset()

class OrderItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    lookup_field = 'slug'

class ShippingListAPIView(generics.ListCreateAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    # pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class ShippingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class DiscountDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class DiscountListAPIView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)