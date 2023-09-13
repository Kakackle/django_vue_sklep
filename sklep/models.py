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
    active = models.BooleanField(default=False)
    product_count = models.PositiveIntegerField(default=0, blank=True)
    sales_count = models.PositiveIntegerField(default=0, blank=True)
    view_count = models.PositiveIntegerField(default=0, blank=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    rating_average = models.DecimalField(default=0, decimal_places=2,
                                         max_digits=3,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        blank=True
    )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, default="temp")
    country = models.CharField(max_length=50, choices=COUNTRIES)

    class Meta: 
        ordering = ['-name']

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
    slug = models.SlugField(unique=True, blank=True, default="temp")

    class Meta: 
        ordering = ['-name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

class Shipping(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=10.0, decimal_places=2, max_digits=6,
                              validators=[MinValueValidator(0.0)])
    days_minimum = models.PositiveIntegerField(default=1)
    slug = models.SlugField(unique=True, default='temp', blank=True)

    class Meta: 
        ordering = ['-name']

    def __str__(self):
        return '[shipping] ' + self.name
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

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
    SIZE_TYPES = [
        ('compact', 'compact'),
        ('full', 'full sized'),
        ('double', 'double')
    ]
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(default=100.0, decimal_places=2, max_digits=8,
                              validators=[MinValueValidator(0.0)])
    main_product_image = models.ImageField(blank=True, upload_to=upload_to_product,
                                           default="../static/img/default_effect.jpg")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='products')
    name = models.CharField(max_length=100)
    rating_average = models.DecimalField(default=0, decimal_places=2, max_digits=3,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        blank=True
    )
    warranty = models.PositiveIntegerField(default=2, blank=True)
    bypass = models.BooleanField(default=True, blank=True, help_text="Only required if product of type 'effect'",)
    manufacturer = models.ForeignKey(Manufacturer, related_name="products",
                                     on_delete=models.CASCADE)
    # shipping = models.FloatField(default=10.0,
    #     validators=[MinValueValidator(0.0),],
    #     blank=True)
    effect_type = models.ForeignKey(EffectType, null=True, blank=True,
                                    related_name="products",
                                    on_delete=models.SET_NULL
                                    , help_text="Only required if product of type 'effect'")
    power_type = models.CharField(max_length=50, choices=POWER_TYPES,
                                   blank=True,
                                    help_text="Only required if product of type 'effect'")
    quantity = models.PositiveIntegerField(default=5, blank=True)
    discount = models.DecimalField(default=0.0, decimal_places=2, max_digits=3,
                                 validators=[MinValueValidator(0.0)],
                                 blank=True)
    slug = models.SlugField(unique=True, default="temp", blank=True)
    about = models.TextField(max_length=2000, null=True, blank=True)
    technical = models.TextField(max_length=2000, null=True, blank=True)
    other = models.TextField(max_length=2000, null=True, blank=True)
    character = models.CharField(max_length=100, blank=True,
                                 help_text="eg. 'fuzzy', 'slick'")
    size_type = models.CharField(max_length=25, choices=SIZE_TYPES, blank=True,
                                 help_text="Only required if product of type 'effect'",
                                 default="compact")
    view_count = models.PositiveIntegerField(blank=True, default=0)
    bought_count = models.PositiveIntegerField(blank=True, default=0)

    class Meta: 
        ordering = ['-name']

    def __str__(self):
        # return '[prod] ' + self.name
        return self.slug
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
class ProductImage(models.Model):
    # random_str = get_random_string(length=6)
    def image_dir(self, filename):
        random_str = get_random_string(length=6)
        return 'images/{product}/images/{random}-{filename}'.format(
            filename=filename, product=self.product.slug,
            random=random_str
        )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="product_images")
    image = models.ImageField(upload_to=image_dir)
    slug = models.SlugField(unique=True, default='temp', blank=True)

    class Meta: 
        ordering = ['-slug']

    def __str__(self):
        # random_str = get_random_string(length="6")
        return self.slug
    
    def save(self, *args, **kwargs):
        random_str = get_random_string(length=6)
        if self.slug == "temp":
            self.slug = slugify(self.product.slug + 'image' + '-' + random_str + str(self.product.pk))
        return super().save(*args, **kwargs)

class Review(models.Model):
    author = models.ForeignKey(User, related_name="reviews",
                               null=True,
                               on_delete=models.SET_NULL)
    message = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    product = models.ForeignKey(Product, related_name="reviews",
                                on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100) 
    slug = models.SlugField(unique=True, default="temp")
    liked_by = models.ManyToManyField(User, blank=True, related_name="liked_comments")
    like_count = models.PositiveIntegerField(blank=True, default=0)

    class Meta: 
        ordering = ['-date_created']

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.product.slug + 'review' + self.author.username)
        return super().save(*args, **kwargs)

# TODO: jakis sposob na sluga czy cos takiego, albo wystarczy po userze?
class Cart(models.Model):
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="carts", blank=True)
    sum_items = models.PositiveIntegerField(default=0, blank=True)
    sum_cost = models.DecimalField(default=0.0, blank=True, decimal_places=2,
                                   max_digits = 8,
                                    validators=[MinValueValidator(0.0)])
    shipping_method = models.ForeignKey(Shipping, null=True, on_delete=models.SET_NULL)
    shipping_cost = models.DecimalField(default=10.0, blank=True, decimal_places=2,
                                        max_digits=6,
                                         validators=[MinValueValidator(0.0)])
    discount = models.DecimalField(default=0.0, blank=True, decimal_places=2,
                                   max_digits=3,
                                  validators=[MinValueValidator(0.0),
                                               MaxValueValidator(1.0)])
    slug = models.SlugField(unique=True, default="temp")

    def __str__(self):
        return self.user.username + '[cart]'
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.user.username + '-cart')
        return super().save(*args, **kwargs)

# TODO: tutaj uzytkownik moze miec wiele orders, wiec albo po userze albo juz slug by sie przyal z data itd
# TODO: w sumie pk juz jest globalnym systemem sledzenia wszystkich orders
# od wszystkich uzytkownikow...
class Order(models.Model):
    ORDER_STATUS = [
        ('paid', 'paid'),
        ('sent', 'sent'),
        ('delivered', 'delivered'),
        ('progress', 'in progress')
    ]
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    products = models.ManyToManyField(Product, related_name="orders", blank=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default='progress')
    sum_cost = sum_cost = models.DecimalField(default=0.0, blank=True,
                                              max_digits=8,
                                              decimal_places=2,
                                 validators=[MinValueValidator(0.0)])
    shipping_method = models.ForeignKey(Shipping, null=True, on_delete=models.SET_NULL)
    shipping_cost = models.DecimalField(default=10.0, blank=True,
                                        decimal_places=2, max_digits=5,
                                        validators=[MinValueValidator(0.0)])
    
    class Meta: 
        ordering = ['-date_updated']

    def __str__(self):
        return self.user.username + '[order]'



