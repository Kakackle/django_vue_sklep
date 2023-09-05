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
    class Meta:
        model = Product
        fields = ('type', 'name', 'price', 'main_product_image', 'warranty',
                  'bypass', 'manufacturer', 'shipping', 'quantity', 'discount',
                  'about', 'technical', 'other')