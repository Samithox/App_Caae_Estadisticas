from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ('rut_Cliente', 'nombre_Cliente','email_Cliente','telefono_Cliente','tipo_Reserva',)