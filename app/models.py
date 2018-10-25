from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    rut_Cliente = models.CharField(max_length=9)
    nombre_Cliente = models.CharField(max_length=50)
    email_Cliente = models.CharField(max_length=100)
    telefono_Cliente = models.IntegerField()
    RESERVA = 'Con Reserva'
    SIN_RESERVA = 'Sin Reserva'
    TIPO_RESERVA_CHOICES = (
        (RESERVA, 'Con Reserva'),
        (SIN_RESERVA, 'Sin Reserva'),
        )
    tipo_Reserva = models.CharField(max_length=20,choices=TIPO_RESERVA_CHOICES,blank=True)
    objects  = models.Manager()

    def __str__(self):
        return '%s' % (self.rut_Cliente)
