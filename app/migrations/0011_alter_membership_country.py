# Generated by Django 4.1 on 2022-08-19 14:58

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_cover_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='country',
            field=django_countries.fields.CountryField(default='UA', max_length=2),
        ),
    ]