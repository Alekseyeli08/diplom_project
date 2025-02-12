# Generated by Django 5.1.3 on 2024-12-04 10:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("reservation", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reservations",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AddField(
            model_name="reservations",
            name="name_table",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="reservation.table",
                verbose_name="Номер стола",
            ),
        ),
    ]
