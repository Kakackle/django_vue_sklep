from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
# from users.models import Address, UserProfile

class Address(models.Model):
    country = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    street_number = models.PositiveIntegerField()
    zipcode = models.CharField(max_length=8)
    user = models.ForeignKey(User, related_name="address", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + '-address-' + slugify(self.street) + str(self.street_number)

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

        # calculate total sales and average rating
        # sales = 0
        rating = 0
        # manufacturer has to exist before relationships can be used
        if self.pk:
            for product in self.products.all():
                # sales += product.bought_count
                rating += product.rating_average
            # self.sales_count = sales
            if self.products.count() != 0:
                self.rating_average = rating/self.products.count()
            else:
                self.rating_average = 0
            self.product_count = self.products.count()
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
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
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
    bypass = models.BooleanField(default=True, blank=True, null=True, help_text="Only required if product of type 'effect'",)
    manufacturer = models.ForeignKey(Manufacturer, related_name="products",
                                     on_delete=models.CASCADE)
    effect_type = models.ForeignKey(EffectType, null=True, blank=True,
                                    related_name="products",
                                    on_delete=models.SET_NULL
                                    , help_text="Only required if product of type 'effect'")
    power_type = models.CharField(max_length=50, choices=POWER_TYPES,
                                   blank=True, null=True,
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
        sum_ratings = 0
        # product instance must exist
        if self.pk:
            for review in self.reviews.all():
                sum_ratings += review.rating
            if self.reviews.count() != 0:
                self.rating_average = sum_ratings/self.reviews.count()
            else: self.rating_average = 0

            # quant = 0
            # for order in self.orders.all():
            #     quant += order.quantity
            # self.bought_count = quant
        return super().save(*args, **kwargs)
    
    @property
    def price_discounted(self):
        return self.price * (1-self.discount)
    
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

class Discount(models.Model):
    name = models.CharField(unique=True, max_length=30)
    discount = models.DecimalField(default=0.0, decimal_places=2, max_digits=3,
                                 validators=[MinValueValidator(0.0)],)
    date_valid = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, default="temp")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Cart(models.Model):
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product, related_name="carts", blank=True)
    sum_items = models.PositiveIntegerField(default=0, blank=True)
    sum_cost = models.DecimalField(default=0.0, blank=True, decimal_places=2,
                                   max_digits = 8,
                                    validators=[MinValueValidator(0.0)])
    slug = models.SlugField(unique=True, default="temp")

    def __str__(self):
        return self.user.username + '-cart'
    
    def save(self, *args, **kwargs):
        if self.slug == "temp":
            self.slug = slugify(self.user.username + '-cart')

        # cart must exist
        if self.pk:
            if self.sum_cost == 0:
                cost = 0
                self.sum_items = self.items.count()
                for item in self.items.all():
                    cost += item.product.price_discounted
                self.sum_cost = cost
        return super().save(*args, **kwargs)

class CartItem(models.Model):
    product = models.ForeignKey(Product, related_name="carts", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart.slug + ' - ' + self.product.slug

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
    # products = models.ManyToManyField(Product, related_name="orders", blank=True)
    # items = models.ManyToManyField(CartItem, related_name="orders", blank=True)
    address = models.ForeignKey(Address, related_name="orders", on_delete=models.SET_NULL,
                                null=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default='progress')
    discount = models.DecimalField(default=0.0, blank=True, decimal_places=2,
                                   max_digits=3,
                                  validators=[MinValueValidator(0.0),
                                               MaxValueValidator(1.0)])
    sum_cost = models.DecimalField(default=0.0, blank=True,
                                              max_digits=8,
                                              decimal_places=2,
                                 validators=[MinValueValidator(0.0)])
    sum_items = models.PositiveIntegerField(default=0)
    shipping_method = models.ForeignKey(Shipping, null=True, on_delete=models.SET_NULL)
    shipping_cost = models.DecimalField(default=10.0, blank=True,
                                        decimal_places=2, max_digits=5,
                                        validators=[MinValueValidator(0.0)])
    
    class Meta: 
        ordering = ['-date_updated']

    def __str__(self):
        return self.user.username + '-order' + '-' + str(self.pk)
    
    def save(self, *args, **kwargs):
        #order instance must exist
        if self.pk:
            self.sum_items = self.items.count()
            self.shipping_cost = self.shipping_method.price
            cost = 0
            for item in self.items.all():
                cost += item.product.price_discounted
            self.sum_cost = cost
            self.sum_cost = self.sum_cost * (1-self.discount)
            if self.sum_cost < 250:
                self.sum_cost += self.shipping_cost
        return super().save(*args, **kwargs)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'order-' + str(self.order.pk) + '-' + self.product.slug



