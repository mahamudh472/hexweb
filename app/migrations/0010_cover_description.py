# Generated by Django 4.1 on 2022-08-19 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_people_membership_person_membershipperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]