# Generated by Django 4.0.6 on 2023-11-24 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crops', '0007_rename_wheat_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Wheat',
        ),
    ]
