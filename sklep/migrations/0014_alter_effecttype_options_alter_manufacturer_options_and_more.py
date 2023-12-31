# Generated by Django 4.2.4 on 2023-09-08 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0013_alter_product_bypass_alter_product_effect_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='effecttype',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date_updated']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['-slug']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='shipping',
            options={'ordering': ['-name']},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_update',
            new_name='date_updated',
        ),
    ]
