from django.urls import path

from reservation.apps import ReservationConfig
from reservation.views import (
    ReservarionCreateView,
    Reservation_history_ListView,
    ReservationUpdateView,
    TableListView,
    contacts,
    feedback,
    history,
    home,
    reservation_activity,
    reservations_confirmation,
)

app_name = ReservationConfig.name


urlpatterns = [
    path("", home, name="home"),
    path("history/", history, name="history"),
    path("create/", ReservarionCreateView.as_view(), name="reservation_create"),
    path("table_list/", TableListView.as_view(), name="table_list"),
    path(
        "reservations_history_list/",
        Reservation_history_ListView.as_view(),
        name="reservations_history_list",
    ),
    path("activity/<int:pk>/", reservation_activity, name="reservation_activity"),
    path(
        "edit/<int:pk>/update/",
        ReservationUpdateView.as_view(),
        name="reservations_update",
    ),
    path(
        "confirm/<int:pk>/", reservations_confirmation, name="reservations_confirmation"
    ),
    path("feedback/", feedback, name="feedback"),
    path("contacts/", contacts, name="contacts"),
]
