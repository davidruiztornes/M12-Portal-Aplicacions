# Generated by Django 3.2.2 on 2021-05-10 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
    ]
