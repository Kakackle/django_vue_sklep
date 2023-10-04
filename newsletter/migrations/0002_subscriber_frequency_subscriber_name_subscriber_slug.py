# Generated by Django 4.2.4 on 2023-10-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='frequency',
            field=models.IntegerField(choices=[(7, 'weekly'), (14, 'bi-weekly'), (31, 'monthly')], default=7),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='name',
            field=models.CharField(default='test user', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='slug',
            field=models.SlugField(default='temp', unique=True),
        ),
    ]
