# Generated by Django 4.0.4 on 2022-05-10 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_type',
            new_name='type',
        ),
    ]
