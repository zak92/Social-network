# Generated by Django 3.0.3 on 2022-02-22 17:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snapp', '0026_remove_appuser_friends'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FriendList',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='friends',
            new_name='contacts',
        ),
    ]
