# Generated by Django 3.2.5 on 2021-07-21 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_userprofile_profile_pricture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_pricture',
            new_name='profile_picture',
        ),
    ]