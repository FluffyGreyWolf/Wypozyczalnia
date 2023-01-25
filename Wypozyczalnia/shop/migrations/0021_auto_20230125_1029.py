# Generated by Django 3.2.16 on 2023-01-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20230124_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='shipping',
        ),
        migrations.RemoveField(
            model_name='product',
            name='warranty',
        ),
        migrations.AddField(
            model_name='product',
            name='cena_wypozyczenia',
            field=models.IntegerField(default=0, help_text='Cena wypożyczenia produktu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='dzieci',
            field=models.BooleanField(default=False, help_text='Czy gra jest przeznaczona dla dzieci'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='trudnosc',
            field=models.CharField(default=1, help_text='Poziom trundości gry Łatwa/Umiarkowana/Trudna', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='wypozyczenie',
            field=models.CharField(default=7, help_text='WDługośc okresu wypożyczenia', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(help_text='Kategoria produktu', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(help_text='Opis produktu'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Nazwa produktu', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(help_text='Cena kupna produktu'),
        ),
    ]