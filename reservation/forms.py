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
    class Meta:
        model = Reservations
        fields = ["name_table", "date", "time", "quantity", "comment", "period"]

    # clean метод на time
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
