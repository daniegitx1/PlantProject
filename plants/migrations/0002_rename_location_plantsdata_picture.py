# Generated by Django 5.0.7 on 2024-07-16 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantsdata',
            old_name='location',
            new_name='picture',
        ),
    ]
