# Generated by Django 3.2.4 on 2021-06-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshopapp', '0004_mascota_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.IntegerField(verbose_name='edad'),
        ),
    ]
