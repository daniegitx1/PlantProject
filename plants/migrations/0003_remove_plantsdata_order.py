# Generated by Django 5.0.7 on 2024-07-16 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_rename_location_plantsdata_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantsdata',
            name='order',
        ),
    ]