from datetime import datetime, time, timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField, DateInput, ModelForm, Textarea, TextInput
from django.utils import timezone

from reservation.models import Reservations


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ReservationForm(StyleFormMixin, ModelForm):
    TIME_CHOICES = [(time(hour), f"{hour:02d}:00") for hour in range(10, 20)]
    TIME_PERIOD = [(1, '1 час'), (2, '2 часа')]
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Дата')
    time = forms.ChoiceField(choices=TIME_CHOICES, label='Время')
    period = forms.ChoiceField(choices=TIME_PERIOD, label='Продолжительность')
    comment = forms.CharField(widget=forms.Textarea, required=False, label='Комментарии')

    class Meta:
        model = Reservations
        fields = ["name_table", "date", "time", "quantity", "period", "comment"]

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get("name_table")
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if date and time and table:
            if Reservations.objects.filter(
                name_table=table, date=date, time=time, is_active=True
            ).exists():
                raise ValidationError("Столик уже забронирован на данное время")

        return cleaned_data


class Reservation_history_Form(StyleFormMixin, ModelForm):
    class Meta:
        model = Reservations
        fields = ["name_table", "date", "is_active"]
