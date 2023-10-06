# signals
from django.dispatch import receiver
from django.db.models.signals import ( post_save, post_delete)
from sklep.models import Manufacturer, Product, Order

@receiver(post_save, sender=Product)
def manufacturer_product_created(sender ,instance, created, *args, **kwargs):
    if created:
        man = Manufacturer.objects.get(id=instance.manufacturer.id)
        man.product_count += 1
        man.save()
    else:
        pass

@receiver(post_delete, sender=Product)
def manufacturer_product_deleted(sender ,instance, *args, **kwargs):
    man = Manufacturer.objects.get(id=instance.manufacturer.id)
    man.product_count -= 1
    man.save()

@receiver(post_save, sender=Order)
def post_order_bought_count(sender, instance, created, *args, **kwargs):
    # product = Product.objects.get(id=instance.)
    if created:
        for item in instance.items.all():
            product = Product.objects.get(id=item.product.id)
            product.bought_count += item.quantity
            product.save()
            man = Manufacturer.objects.get(id=item.product.manufacturer.id)
            man.sales_count += item.quantity
            man.save()