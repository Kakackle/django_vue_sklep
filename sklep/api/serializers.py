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

class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )
    owner = UserSerializer(read_only=True)
    manufacturer = ManufacturerSerializer(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"
        lookup_field = 'slug'
    
    