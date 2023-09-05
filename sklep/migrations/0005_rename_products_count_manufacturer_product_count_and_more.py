# Generated by Django 4.2.4 on 2023-09-05 08:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sklep', '0004_product_about_product_other_product_technical'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturer',
            old_name='products_count',
            new_name='product_count',
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='view_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='bought_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='view_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='like_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]