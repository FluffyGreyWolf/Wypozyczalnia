# Generated by Django 3.2.5 on 2021-08-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_orderhistory_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.CharField(default='No warranty', help_text='Warranty length in years', max_length=30),
            preserve_default=False,
        ),
    ]
