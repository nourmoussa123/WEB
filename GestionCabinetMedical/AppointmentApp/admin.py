from django.contrib import admin
from AppointmentApp.models import Appointment

@admin.site.register(Appointment)
class AppointmentAdminPersonaliser(admin.ModelAdmin):
    list_display = ('reason', 'appointment_date', 'status')
    list_filter = ('status', 'reson')
    
# Register your models here.
