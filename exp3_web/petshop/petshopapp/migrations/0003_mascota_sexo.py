# Generated by Django 3.2.4 on 2021-06-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshopapp', '0002_auto_20210617_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(default=30, max_length=10, verbose_name='sexo'),
            preserve_default=False,
        ),
    ]
