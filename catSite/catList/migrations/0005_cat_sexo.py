# Generated by Django 5.1.3 on 2024-11-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catList', '0004_alter_cat_cropping'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='sexo',
            field=models.CharField(choices=[('macho', 'Macho'), ('hembra', 'Hembra')], default='macho', max_length=6),
        ),
    ]
