from django.contrib import admin
from .models import Room, Booking

admin.site.register(Room)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'phone_number', 'persons', 'check_in', 'check_out')
    search_fields = ('user', 'phone_number', )

admin.site.register(Booking, BookingAdmin)
