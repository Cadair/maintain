# Generated by Django 3.1.3 on 2020-12-11 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("maintain", "0011_remove_mileage_log_timestamp"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mileage_log",
            old_name="timestamp_date",
            new_name="timestamp",
        ),
    ]
