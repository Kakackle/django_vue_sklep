from rest_framework import serializers
from sklep.models import Profile, Product

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    department = serializers.ChoiceField(choices=Profile.USER_TYPE)
    class Meta:
        model = Profile
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Product
        fields = "__all__"
    