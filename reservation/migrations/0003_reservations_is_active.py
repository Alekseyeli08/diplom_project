# Generated by Django 4.1 on 2024-12-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservations",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Забронировано"),
        ),
    ]