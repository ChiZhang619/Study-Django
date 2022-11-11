# Generated by Django 3.2.5 on 2022-11-11 12:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0004_fav'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='favorites',
            field=models.ManyToManyField(related_name='favorite_things', through='ads.Fav', to=settings.AUTH_USER_MODEL),
        ),
    ]
