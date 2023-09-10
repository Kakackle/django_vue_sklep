from rest_framework import serializers
from sklep.models import (Product, Manufacturer, EffectType,
                          Shipping, ProductImage, Review, Cart,
                          Order)
from users.models import UserProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    favourite_products = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'id',
                  'favourite_products')
        lookup_field = 'username'

class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )
    user = UserSerializer(read_only=True)
    # department = serializers.ChoiceField(choices=Profile.USER_TYPE)
    class Meta:
        model = UserProfile
        fields = "__all__"

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
    product = serializers.SlugRelatedField(Product, read_only=True)
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
    class Meta:
        model = Product
        fields = "__all__"
        lookup_field = 'slug'

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    shipping_method = ShippingSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = "__all__"
        lookup_field = 'slug'

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    shipping_method = ShippingSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = "__all__"
        lookup_field = 'slug'
    