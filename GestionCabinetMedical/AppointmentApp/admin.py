from django.contrib import admin
from AppointmentApp.models import *

@admin.register(Appointment)
class AppointmentAdminPersonaliser(admin.ModelAdmin):
    list_display = ('reason', 'appointment_date', 'status')
    list_filter = ('status', 'reason')
    
# Register your models here.
