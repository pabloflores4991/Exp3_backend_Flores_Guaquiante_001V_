# Generated by Django 3.2.4 on 2021-06-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshopapp', '0010_auto_20210621_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
