# Generated by Django 5.1.3 on 2024-12-04 10:24

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reservations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_name", models.CharField(max_length=50, verbose_name="Фамилия")),
                (
                    "date",
                    models.DateField(default=datetime.date.today, verbose_name="Дата"),
                ),
                ("time", models.TimeField(default=datetime.time, verbose_name="Время")),
                ("quantity", models.SmallIntegerField(verbose_name="Кол-во персон")),
                (
                    "comment",
                    models.CharField(max_length=200, verbose_name="Комментарии"),
                ),
                (
                    "period",
                    models.SmallIntegerField(
                        verbose_name="Продолжительность бронирования"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Table",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Номер стола")),
                (
                    "comment",
                    models.CharField(max_length=100, verbose_name="Комментарии"),
                ),
            ],
            options={
                "verbose_name": "стол",
                "verbose_name_plural": "столы",
            },
        ),
    ]
