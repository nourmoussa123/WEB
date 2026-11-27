from django.contrib import admin
from AccountApp.models import Doctor,Patient,Specialty,User

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Specialty)
admin.site.register(User)

# Register your models here.
