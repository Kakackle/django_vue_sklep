# Generated by Django 4.2.4 on 2023-09-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favourite_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]