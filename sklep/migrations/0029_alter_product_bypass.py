# Generated by Django 4.2.4 on 2023-10-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0028_product_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bypass',
            field=models.BooleanField(blank=True, default=True, help_text="Only required if product of type 'effect'", null=True),
        ),
    ]
