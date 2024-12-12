from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    first_name = models.CharField(max_length=100, verbose_name="имя пользователя")
    last_name = models.CharField(**NULLABLE, max_length=100, verbose_name="фамилия")
    phone = models.CharField(**NULLABLE, max_length=40, verbose_name="номер телефона")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}{self.first_name}"
