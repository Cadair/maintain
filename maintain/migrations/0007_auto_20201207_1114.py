# Generated by Django 3.1.3 on 2020-12-07 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("maintain", "0006_auto_20201126_0918"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="default",
        ),
        migrations.RemoveField(
            model_name="car",
            name="starting_mileage",
        ),
    ]
