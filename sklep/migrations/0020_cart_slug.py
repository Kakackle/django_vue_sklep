# Generated by Django 4.2.4 on 2023-09-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0019_product_character_product_size_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='slug',
            field=models.SlugField(default='temp', unique=True),
        ),
    ]
