# Generated by Django 3.0.3 on 2022-02-14 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snapp', '0009_auto_20220214_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='description',
        ),
    ]