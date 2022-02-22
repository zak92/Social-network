# Generated by Django 3.0.3 on 2022-02-22 17:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snapp', '0027_auto_20220222_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
    ]
