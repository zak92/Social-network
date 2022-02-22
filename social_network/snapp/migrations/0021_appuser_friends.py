# Generated by Django 3.0.3 on 2022-02-22 15:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snapp', '0020_galleryimage_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
