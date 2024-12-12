import datetime

from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Table(models.Model):
    name = models.CharField(max_length=50, verbose_name="Номер стола")
    comment = models.CharField(max_length=100, verbose_name="Комментарии")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "стол"
        verbose_name_plural = "столы"


class Reservations(models.Model):
    name_table = models.ForeignKey(
        Table, on_delete=models.CASCADE, verbose_name="Номер стола"
    )
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    date = models.DateField(default=datetime.date.today, verbose_name="Дата")
    time = models.TimeField(default=datetime.time, verbose_name="Время")
    quantity = models.SmallIntegerField(verbose_name="Кол-во персон")
    comment = models.CharField(max_length=200, verbose_name="Комментарии")
    period = models.SmallIntegerField(verbose_name="Продолжительность бронирования")
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="Владелец", **NULLABLE
    )
    is_active = models.BooleanField(default=True, verbose_name="Забронировано")

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "Бронировние"
        verbose_name_plural = "Бронировние"
