from django.shortcuts import get_object_or_404
from sklep.models import (Product, Manufacturer, User, EffectType, Shipping, ProductImage,
                          Cart, CartItem, Order, Review, Discount, Address,
                          OrderItem)
from users.models import UserProfile
from sklep.api.serializers import (ProductSerializer, ManufacturerSerializer,
                                   UserSerializer, ProfileSerializer,
                                   EffectTypeSerializer, ShippingSerializer,
                                   OrderSerializer, CartSerializer,
                                   ProductImageSerializer, ReviewSerializer,
                                   CartItemSerializer, DiscountSerializer,
                                   AddressSerializer, OrderItemSerializer)
from .permissions import IsOwnerOrReadOnly
from.pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.parsers import FormParser, MultiPartParser

from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter, BooleanFilter, ChoiceFilter, NumberFilter

from decimal import Decimal
from rest_framework.exceptions import APIException

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

class ProductAddToCartAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,) 

    def patch(self, request, *args, **kwargs):
        print('update request data:', self.request.data)
        return self.partial_update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        user = self.request.user
        cart = user.cart

        product_slug = self.kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)

        #if a cartItem object for specifiec product already exists
        try: 
            item = CartItem.objects.get(product = product)
        # if (item):
        #if product quantity if enough to add another to cartItem object
            if (item.quantity + 1 <= product.quantity):
                item.quantity += 1
                item.save()
                cart.sum_items += 1
                cart.sum_cost += (product.price * (1-product.discount))
                cart.save()
            else:
                raise APIException(detail="Product stock too low!")
                # return JsonResponse({'message': 'product stock too low'},status=400)
                # return Response({'message': 'product stock too low'}, status=status.HTTP_400_BAD_REQUEST)

        except CartItem.DoesNotExist:
        # else:
            item = CartItem.objects.create(product=product, cart=cart, quantity=1)
            item.save()
            cart.sum_items += 1
            cart.sum_cost += (product.price * (1-product.discount))
            cart.save()

        cart_items = list(cart.items.all().values())
                            #   .values_list('slug', flat=True))
            
            # print('fav products: ', favourite_products)
        return JsonResponse({'cart_items': cart_items, 
                                'message': 'added to cart'},status=200)
    
class ProductSubtractFromCartAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,) 

    def patch(self, request, *args, **kwargs):
        print('update request data:', self.request.data)
        return self.partial_update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        user = self.request.user
        cart = user.cart

        product_slug = self.kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)

        try: 
            item = CartItem.objects.get(product = product)
        except CartItem.DoesNotExist:
            cart_items = list(cart.items.all().values())
            return JsonResponse({'cart_items': cart_items, 
                             'message': 'item not in cart'},status=404)
        
        # jesli to ostatni przedmiot tego typu
        if (item.quantity == 1):
            item.delete()
            cart.sum_items -= 1
            cart.sum_cost -= (product.price * (1-product.discount))
            cart.save()
        else:
            item.quantity -= 1
            item.save()
            cart.sum_items -= 1
            cart.sum_cost -= (product.price * (1-product.discount))
            cart.save()

        cart_items = list(cart.items.all().values())
                        #   .values_list('slug', flat=True))
        return JsonResponse({'cart_items': cart_items, 
                             'message': 'removed from cart'},status=200)
    
class ProductRemoveFromCartAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,) 

    def patch(self, request, *args, **kwargs):
        print('update request data:', self.request.data)
        return self.partial_update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        user = self.request.user
        cart = user.cart

        product_slug = self.kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)

        try: 
            item = CartItem.objects.get(product=product)
            # cart.items.remove(item)
            item.delete()
            cart.sum_cost -= (product.price * (1-product.discount))
            cart.save()
        except CartItem.DoesNotExist:
            cart_items = list(cart.items.all().values())
            return JsonResponse({'cart_items': cart_items, 
                             'message': 'item not in cart'},status=404)

        cart_items = list(cart.items.all().values())
                        #   .values_list('slug', flat=True))
        return JsonResponse({'cart_items': cart_items, 
                             'message': 'removed from cart'},status=200)

class CartClearAPIView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def patch(self, request, *args, **kwargs):
        print('update request data:', self.request.data)
        return self.partial_update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        # user = self.request.user
        cart = Cart.objects.get(slug=self.kwargs.get('slug'))
        for item in cart.items.all():
            item.delete()
        cart.sum_items = 0
        cart.sum_cost = 0
        cart.save()
        return JsonResponse({'message': 'cart cleaned'},status=200)

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

    # def get_object(self):
    #     obj = get_object_or_404(self.get_queryset(), slug=self.kwargs["slug"])
    #     self.check_object_permissions(self.request, obj)
    #     return obj

class ProductFilters(FilterSet):
    manufacturer = CharFilter(field_name='manufacturer__slug', lookup_expr='contains')
    type = CharFilter(field_name='type', lookup_expr='contains')
    price_lte = NumberFilter(field_name='price', lookup_expr="lte")
    price_gte = NumberFilter(field_name='price', lookup_expr="gte")
    discount_gte = NumberFilter(field_name="discount", lookup_expr="gte")
    rating_gte = NumberFilter(field_name="rating_average", lookup_expr="gte")
    class Meta:
        model = Product
        fields = ['manufacturer__slug', 'type', 'price', 'discount', 'rating_average']

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

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'token': csrf_token})

# ====================================================================

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

        # discount_slug = self.request.data.get('discount')
        # if (discount_slug):
        #     discount = Discount.objects.get(slug=discount_slug)
        #     
        # else:
        #     sum_cost = cart.sum_cost

        # discount przychodzi w wartosci liczbowej aktualnie
        discount = Decimal(self.request.data.get('discount'))
        sum_cost = Decimal(cart.sum_cost) * (1 - discount)
        shipping_slug = self.request.data.get('shipping_method')
        shipping_method = Shipping.objects.get(slug = shipping_slug)
        shipping_cost = shipping_method.price
        sum_cost += shipping_cost
        status = 'progress'
        user = user

        # serializer.save(user=user, items=items, address=address, status=status,
        #         discount=discount, sum_cost = sum_cost, shipping_method=shipping_method,
        #         shipping_cost=shipping_cost)
        
        order = Order.objects.create(user=user, address=address, status=status,
                discount=discount, sum_cost = sum_cost, shipping_method=shipping_method,
                shipping_cost=shipping_cost)

        # items = []
        for item in cart.items.all():
            order_item = OrderItem.objects.create(product=item.product,
                                              quantity=item.quantity,
                                              order=order)
        
        return JsonResponse({'data': serializer.data, 
                        'message': 'added to orders'},status=200)


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    lookup_field = 'slug'

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


class CartListAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class CartDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) 
    lookup_field = 'slug'

class CartItemListAPIView(generics.ListCreateAPIView):
    # queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        cart_slug = self.kwargs.get('slug')
        cart = Cart.objects.get(slug=cart_slug)
        return CartItem.objects.filter(cart=cart)
        # return super().get_queryset()

class CartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
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

class ReviewFilters(FilterSet):
    product = CharFilter(field_name='product__slug', lookup_expr='contains')
    author = CharFilter(field_name='author__username', lookup_expr='iexact')

    class Meta:
        model = Review
        fields = ['product__slug', 'author__username']

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReviewFilters
    permission_classes = (IsAuthenticatedOrReadOnly,) 

    def post(self, request, *args, **kwargs):
        print('received request: ', request.data)
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
    
    def perform_create(self, serializer):
        product_slug = self.request.data.get('product')
        product = Product.objects.get(slug=product_slug)
        author_username = self.request.data.get('author')
        author = User.objects.get(username=author_username)
        serializer.save(product=product, author=author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class ReviewLikeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,) 
    lookup_field = 'slug'

    def patch(self, request, *args, **kwargs):
        print('update request data:', self.request.data)
        return self.partial_update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        # print('update request data:', self.request.data)
        # post wybrany przez endpoint
        review_slug = self.kwargs.get('slug')
        review = Review.objects.get(slug=review_slug)
        
        user_slug = self.request.data.get('user')
        user = User.objects.get(username=user_slug)
        
        if user not in review.liked_by.all():
            review.liked_by.add(user)
            review.like_count +=1
            review.save()
        else:
            review.liked_by.remove(user)
            review.like_count -=1
            review.save()

        liked_by_names = list(review.liked_by.all().values_list('username', flat=True))

        return JsonResponse({'liked_by': liked_by_names, 
                             'message': 'liked_by changed'},status=200)
    
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

# class DiscountLookupAPIView(generics.RetrieveAPIView):
#     queryset = Discount.objects.all()
#     serializer_class = DiscountSerializer
#     # lookup_field = 'slug'
#     permission_classes = (IsAuthenticatedOrReadOnly,)

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)