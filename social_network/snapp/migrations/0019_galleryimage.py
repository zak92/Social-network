# Generated by Django 3.0.3 on 2022-02-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapp', '0018_delete_galleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
