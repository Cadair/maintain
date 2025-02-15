# Generated by Django 3.1.3 on 2020-11-19 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maintain", "0003_car_default"),
    ]

    operations = [
        migrations.CreateModel(
            name="MileageLog",
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
                ("timestamp", models.DateTimeField(auto_created=True)),
                ("mileage", models.PositiveIntegerField()),
                (
                    "gas_amount",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=5),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="car",
            name="mileage",
        ),
        migrations.AddField(
            model_name="car",
            name="starting_mileage",
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name="car",
            name="purchase_date",
            field=models.DateField(blank=True),
        ),
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=50)),
                (
                    "logs",
                    models.ManyToManyField(
                        related_name="services", to="maintain.MileageLog"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Part",
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
                ("name", models.CharField(max_length=50)),
                ("number", models.CharField(blank=True, max_length=50)),
                (
                    "logs",
                    models.ManyToManyField(
                        blank=True, related_name="parts", to="maintain.MileageLog"
                    ),
                ),
                (
                    "services",
                    models.ManyToManyField(
                        blank=True, related_name="parts", to="maintain.Service"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="mileagelog",
            name="car",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="logs",
                to="maintain.car",
            ),
        ),
    ]
