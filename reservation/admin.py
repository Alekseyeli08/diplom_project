from django.contrib import admin

from reservation.models import Reservations, Table

admin.site.register(Table)
admin.site.register(Reservations)
