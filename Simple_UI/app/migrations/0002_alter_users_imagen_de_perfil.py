# Generated by Django 3.2.4 on 2021-06-07 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Imagen_de_Perfil',
            field=models.ImageField(upload_to='imagenes/'),
        ),
    ]
