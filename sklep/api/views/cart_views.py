from sklep.models import (Product, CartItem, Cart)
from sklep.api.serializers import (ProductSerializer, CartItemSerializer,
                                   CartSerializer)
from rest_framework import generics
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from sklep.api.permissions import IsUserOrReadOnly
from sklep.api.pagination import CustomPagination

from django.http import JsonResponse

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
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (IsUserOrReadOnly,)

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


class CartListAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class CartDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (IsUserOrReadOnly,)
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