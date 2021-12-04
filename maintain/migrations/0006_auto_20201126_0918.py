# Generated by Django 3.1.3 on 2020-11-26 14:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("maintain", "0005_auto_20201120_0904"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mileage_log",
            name="gas_amount",
        ),
        migrations.RemoveField(
            model_name="part",
            name="logs",
        ),
        migrations.RemoveField(
            model_name="service",
            name="logs",
        ),
        migrations.AddField(
            model_name="service",
            name="log",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="services",
                to="maintain.mileage_log",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="part",
            name="services",
            field=models.ManyToManyField(related_name="parts", to="maintain.Service"),
        ),
        migrations.CreateModel(
            name="Reminder",
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
                ("date", models.DateField(blank=True, null=True)),
                ("mileage", models.PositiveIntegerField(blank=True, null=True)),
                ("completed", models.BooleanField(default=False)),
                (
                    "service",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reminder",
                        to="maintain.service",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fuel",
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
                (
                    "amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "log",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fuel",
                        to="maintain.mileage_log",
                    ),
                ),
            ],
        ),
    ]
