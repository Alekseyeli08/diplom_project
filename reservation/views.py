from datetime import datetime, time, timedelta

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView

from reservation.forms import Reservation_history_Form, ReservationForm
from reservation.models import Reservations, Table


def home(request):
    return render(request, "home.html")


def history(request):
    return render(request, "history.html")


class ReservarionCreateView(CreateView):
    model = Reservations
    form_class = ReservationForm

    def get_success_url(self):
        return reverse(
            "reservation:reservations_confirmation", args=[self.reservation.pk]
        )

    def form_valid(self, form):
        reservation = form.save()
        user = self.request.user
        reservation.owner = user
        reservation.last_name = user.last_name
        reservation.save()
        table = reservation.name_table
        self.reservation = reservation
        date = reservation.date
        filter_reservations = Reservations.objects.filter(
            name_table=table,
            date=form.cleaned_data["date"],
            time=form.cleaned_data["time"],
            is_active=True,
        )

        for reserve in filter_reservations:
            time = reserve.time
            periods = reserve.period
            reserv_time = datetime.combine(date.today(), time) + timedelta(
                hours=periods
            )

            if time <= reservation.time <= reserv_time.time():
                return super().form_invalid(form)
                # return form.add_error('time', 'Столик уже забронирован')

        return super().form_valid(form)


class TableListView(ListView):
    model = Table

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        today = timezone.now().date()

        tables = {}
        for table in self.get_queryset():
            reservations = Reservations.objects.filter(name_table=table, is_active=True)
            times_interval = {}

            for reservation in reservations:
                date = reservation.date
                periods = reservation.period
                time = reservation.time
                s = datetime.combine(date, time) + timedelta(hours=periods)

                # Сохраняем интервалы времени для каждой даты
                if date in times_interval:
                    times_interval[date].append(f"{time}-{s.time()}")
                else:
                    times_interval[date] = [f"{time}-{s.time()}"]

            # Добавляем только если есть временные интервалы
            if times_interval:
                # Сортируем по дате и времени
                sorted_intervals = {}
                for date_key, intervals in sorted(times_interval.items()):
                    sorted_intervals[date_key] = sorted(intervals, key=lambda x: x[0])

                tables[table.name] = sorted_intervals

        context["tables"] = tables
        return context


class Reservation_history_ListView(ListView):
    model = Reservations
    form_class = Reservation_history_Form

    def get_queryset(self, *args, **kwargs):
        owner = self.request.user
        qyryset = super().get_queryset(*args, **kwargs)
        qyryset = qyryset.filter(owner=owner)
        return qyryset


class ReservationUpdateView(UpdateView):
    model = Reservations
    form_class = ReservationForm
    success_url = reverse_lazy("reservation:reservations_history_list")


def reservation_activity(request, pk):
    reservation_item = get_object_or_404(Reservations, pk=pk)
    if reservation_item.is_active:
        reservation_item.is_active = False
    else:
        reservation_item.is_active = True

    reservation_item.save()

    return redirect(reverse("reservation:reservations_history_list"))


def reservations_confirmation(request, pk):
    reserv = get_object_or_404(Reservations, pk=pk)
    return render(
        request, "reservation/reservations_confirmation.html", {"object": reserv}
    )


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Имя пользователя : {name}\nТелефон: {phone}\nСообщение: {message}\n")

    return render(request, "feedback.html")


def contacts(request):
    return render(request, "contacts.html")
