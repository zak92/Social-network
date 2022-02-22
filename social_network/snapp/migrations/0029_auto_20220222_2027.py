# Generated by Django 3.0.3 on 2022-02-22 18:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snapp', '0028_auto_20220222_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contacts',
        ),
        migrations.AddField(
            model_name='appuser',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
    ]
