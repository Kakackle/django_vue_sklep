from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# Create your models here.
def upload_to_manufacturer(instance, filename):
    random_str = get_random_string(length=6)
    return 'images/logos/{random}-{filename}'.format(
        filename=filename, random=random_str
    )


class Manufacturer(models.Model):
    COUNTRIES = [
        ('usa', 'USA'),
        ('poland', 'Poland'),
        ('germany', 'Germany'),
        ('czech', 'Czech Republic')
    ]
    
    owner = models.ForeignKey(User, related_name="manufacturers",
                              on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True, blank=True)
    logo_image = models.ImageField(upload_to=upload_to_manufacturer,
                                   blank=True,
                                   null=True,
                                   default="../static/img/default_logo.png")
    products_count = models.PositiveIntegerField(default=0, blank=True)
    sales_count = models.PositiveIntegerField(default=0, blank=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    rating_average = models.FloatField(default=0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        blank=True
    )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, default="temp")
    country = models.CharField(max_length=50, choices=COUNTRIES)

    def __str__(self):
        return '[man] ' + self.name
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

def upload_to_product(instance, filename):
    random_str = get_random_string(length=6)
    return 'images/products/{random}-{filename}'.format(
        filename=filename, random=random_str
    )

class EffectType(models.Model):
    desc = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    product_count = models.PositiveIntegerField(default=0, blank=True)

class Product(models.Model):
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
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=100.0,
                              validators=[MinValueValidator(0.0)])
    main_product_image = models.ImageField(blank=True, upload_to=upload_to_product,
                                           default="../static/img/default_effect.jpg")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='products')
    name = models.CharField(max_length=100)
    rating_average = models.FloatField(default=0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        blank=True
    )
    warranty = models.PositiveIntegerField(default=2, blank=True)
    bypass = models.BooleanField(default=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, related_name="products",
                                     on_delete=models.CASCADE)
    shipping = models.FloatField(default=10.0,
        validators=[MinValueValidator(0.0),],
        blank=True)
    effect_type = models.ForeignKey(EffectType, null=True, blank=True,
                                    related_name="products",
                                    on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=5, blank=True)
    discount = models.FloatField(default=0.0,
                                 validators=[MinValueValidator(0.0), MaxValueValidator(0.0)],
                                 blank=True)
    slug = models.SlugField(unique=True, default="temp", blank=True)

    def __str__(self):
        return '[prod] ' + self.name
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
class ProductImage(models.Model):

    random_str = get_random_string(length=6)
    
    def image_dir(self, filename):
        # random_str = get_random_string(length=6)
        return 'images/{product}/{random}-{filename}'.format(
            filename=filename, product=self.product.slug,
            random=self.random_str
        )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="product_images")
    image = models.ImageField(upload_to=image_dir)
    slug = models.SlugField(unique=True, default='temp', blank=True)

    def __str__(self):
        # random_str = get_random_string(length="6")
        return self.slug
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.product.slug + 'image' + self.random_str)
        return super().save(*args, **kwargs)

class Review(models.Model):
    author = models.ForeignKey(User, related_name="reviews",
                               null=True,
                               on_delete=models.SET_NULL)
    message = models.CharField(max_length=1000)
    rating = models.FloatField(default=5.0,
                               validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    product = models.ForeignKey(Product, related_name="reviews",
                                on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100) 
    slug = models.SlugField(unique=True, default="temp")

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.product.slug + 'review' + self.author.username)
        return super().save(*args, **kwargs)

class Cart(models.Model):
    user = models.ForeignKey(User, related_name="cart", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="carts", blank=True)
    sum_items = models.PositiveIntegerField(default=0, blank=True)
    sum_cost = models.FloatField(default=0.0, blank=True,
                                 validators=[MinValueValidator(0.0)])
    shipping = models.FloatField(default=10.0, blank=True,
                                 validators=[MinValueValidator(0.0)])
    discount = models.FloatField(default=0.0, blank=True,
                                 validators=[MinValueValidator(0.0)])

class Order(models.Model):
    ORDER_STATUS = [
        ('paid', 'paid'),
        ('sent', 'sent'),
        ('delivered', 'delivered'),
        ('progress', 'in progress')
    ]
    user = models.ForeignKey(User, related_name="order", on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True, blank=True)
    date_update = models.DateTimeField(auto_now=True, blank=True)
    products = models.ManyToManyField(Product, related_name="orders", blank=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS)
    sum_cost = sum_cost = models.FloatField(default=0.0, blank=True,
                                 validators=[MinValueValidator(0.0)])



