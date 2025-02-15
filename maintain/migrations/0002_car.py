# Generated by Django 3.1.3 on 2020-11-17 13:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maintain", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vin", models.CharField(max_length=17)),
                ("make", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
                ("year", models.CharField(max_length=4)),
                ("purchase_date", models.DateField()),
                ("mileage", models.CharField(max_length=6)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cars",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
