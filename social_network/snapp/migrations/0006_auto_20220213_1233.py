# Generated by Django 3.0.3 on 2022-02-13 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snapp', '0005_auto_20220213_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='name',
        ),
    ]
