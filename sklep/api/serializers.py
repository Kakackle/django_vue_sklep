from rest_framework import serializers
from sklep.models import (Product, Manufacturer, EffectType,
                          Shipping, ProductImage, Review, Cart,
                          Order, CartItem, Discount, OrderItem, Address)
from users.models import UserProfile
from newsletter.models import Subscriber
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # favourite_products = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'id',)
        lookup_field = 'username'

class ManufacturerSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )
    owner = UserSerializer(read_only=True)
    products = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='slug')
    class Meta:
        model = Manufacturer
        fields = "__all__"
        lookup_field = 'slug'

class EffectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectType
        fields = ('name', 'desc', 'product_count')
        lookup_field = 'slug'

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ('name', 'price', 'days_minimum')
        lookup_field = 'slug'

class ProductImageSerializer(serializers.ModelSerializer):
    # product = serializers.SlugRelatedField(Product, read_only=True, slug_field='slug')
    product = serializers.StringRelatedField()
    class Meta:
        model = ProductImage
        fields = ('image', 'product')
        lookup_field = 'slug'

class ReviewSerializer(serializers.ModelSerializer):
    # FIXME: dlaczego nie moge tu dac slugrelatedfield? bo jak dam, to zwraca, ze
    # znajduje wiele pol "slug" na produkcie, co jest niemozliwe

    # product = serializers.SlugRelatedField(Product, read_only=True)
    product = serializers.StringRelatedField()
    author = UserSerializer(read_only=True)
    liked_by = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = "__all__"
        lookup_field = 'slug'

class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )
    owner = UserSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    effect_type = serializers.StringRelatedField()
    favourited_by = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Product
        fields = "__all__"
        lookup_field = 'slug'

class CartItemSerializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField()
    product = ProductSerializer(read_only=True)
    cart = serializers.StringRelatedField()
    class Meta:
        model = CartItem
        fields = "__all__"

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, read_only=True)
    # items = CartItemSerializer(many=True, read_only=True)
    items = serializers.StringRelatedField()
    user = UserSerializer(read_only=True)
    shipping_method = ShippingSerializer(read_only=True)
    # discount = DiscountSerializer
    class Meta:
        model = Cart
        fields = "__all__"
        lookup_field = 'slug'

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Address
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField()
    product = ProductSerializer(read_only=True)
    order = serializers.StringRelatedField()
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    # items = ProductSerializer(many=True, read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    shipping_method = ShippingSerializer(read_only=True)
    address = AddressSerializer 
    class Meta:
        model = Order
        fields = "__all__"
        # lookup_field = 'slug'

class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )
    user = UserSerializer(read_only=True)
    favourite_products = ProductSerializer(read_only=True, many=True)
    # department = serializers.ChoiceField(choices=Profile.USER_TYPE)
    class Meta:
        model = UserProfile
        fields = "__all__"

class SubscriberSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Subscriber
        fields = "__all__"