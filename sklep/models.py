from django.db import models
from django.conf import settings

# Create your models here.
# class Profile(models.Model):
#     USER_TYPE = (
#         ('client', 'client user'),
#         ('admin', 'admin user'),
#         ('manufacturer', 'fanufacturer user')
#     )
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
#                              related_name='profile')
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=30, choices=USER_TYPE)
#     mail = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    

class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='products')
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
