# Generated by Django 4.1 on 2022-08-18 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_companyprofile_email_companyprofile_facebook_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='statrt_date',
            new_name='start_date',
        ),
    ]
