# Generated by Django 5.0.1 on 2024-01-23 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='data_created',
            new_name='date_created',
        ),
    ]
