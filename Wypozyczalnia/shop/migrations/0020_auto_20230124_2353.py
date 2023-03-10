# Generated by Django 3.2.16 on 2023-01-24 23:53

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_orderproduct_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='profile_picture',
            field=django_resized.forms.ResizedImageField(crop=None, default='default_profile_picture.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[250, 250], upload_to='user_pictures/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=django_resized.forms.ResizedImageField(crop=None, default='default_profile_picture.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[250, 250], upload_to='user_pictures/'),
        ),
    ]
