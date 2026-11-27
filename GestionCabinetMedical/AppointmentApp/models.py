from django.db import models
from django.core.validators import FileExtensionValidator
from AccountApp.models import Doctor,Patient
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class Appointment(models.Model):
    reason=models.FileField(max_length=255)
    prescription=models.FileField(
            blank=True,
            upload_to='prescriptions/',
            validators=[
                FileExtensionValidator(
                    allowed_extensions=['pdf'],
                    message="accepte uniquement des fichier.pdf"
                )
            ]
        )
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELED = 'canceled', 'Canceled'
    status=models.CharField(max_length=20,
                            choices=Status.choices,
                            default=Status.PENDING)
    duration_minutes=models.PositiveIntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
    appointment_date=models.DateTimeField(blank=False)
    def clean(self):
        modified_date = self._state.adding or(
        Appointment.objects.filter(pk=self.pk,
                                    appointment_date=self.appointment_date).exists())
        if self.appointment_date <= timezone.localdate():
            raise ValidationError("La date du rendez-vous ne peut pas être dans le passé.")
        class Meta():
            ordering=['-appointment_date']
            constraints=[
                models.UniqueConstraint(fields=['doctor','appointment_date'],name='unique_appointment_per_doctor',violation_error_message="Un rendez-vous pour ce médecin à cette date existe déjà.")
            ]
        def __str__(self):
            return f"Appointment: {self.doctor.first_name} "

    
