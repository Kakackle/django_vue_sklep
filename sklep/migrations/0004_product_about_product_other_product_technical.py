# Generated by Django 4.2.4 on 2023-09-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0003_alter_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='other',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='technical',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]