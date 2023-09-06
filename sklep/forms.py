from django import forms
from sklep.models import Product, Manufacturer, EffectType, Review, ProductImage, Cart, Order
from users.models import UserProfile
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

COUNTRIES = [
    ('usa', 'USA'),
    ('poland', 'Poland'),
    ('germany', 'Germany'),
    ('czech', 'Czech Republic')
]

PRODUCT_TYPES = [
    ('effect', 'effect'),
    ('guitar', 'guitar'),
    ('accessory', 'accessory')
    ]

POWER_TYPES = [
    ('9v', '9V Powered'),
    ('12v', '12V Powered'),
    ('inline ', 'Inline Power')
    ]

ORDER_STATUS = [
    ('paid', 'paid'),
    ('sent', 'sent'),
    ('delivered', 'delivered'),
    ('progress', 'in progress')
]

class ProductForm(forms.ModelForm):
    product_image_1 = forms.ImageField(required=False)
    product_image_2 = forms.ImageField(required=False)
    product_image_3 = forms.ImageField(required=False)
    class Meta:
        model = Product
        fields = ('type', 'effect_type', 'power_type', 'name', 'price', 'main_product_image', 'warranty',
                  'bypass', 'manufacturer', 'quantity', 'discount',
                  'about', 'technical', 'other', 'product_image_1',
                  'product_image_2', 'product_image_3')

# TODO: bez wyboru typu i moze czegos inego jeszcze by wypadalo blokowac zmienianie
class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('effect_type', 'power_type', 'name', 'price', 'main_product_image', 'warranty',
                  'bypass', 'manufacturer', 'quantity', 'discount',
                  'about', 'technical', 'other')
        
class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = ProductImage
        fields = ('image',)


# class ManufacturerEditForm(forms.ModelForm)