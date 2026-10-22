from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Cita, Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["nombre", "especie", "raza", "nombre_dueno"]
        labels = {
            "nombre": "Nombre de la mascota",
            "especie": "Especie",
            "raza": "Raza",
            "nombre_dueno": "Nombre del dueño",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej.: Luna"}),
            "especie": forms.Select(attrs={"class": "form-control"}),
            "raza": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej.: Labrador"}),
            "nombre_dueno": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej.: Ana García"}),
        }


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["mascota", "fecha", "hora", "motivo", "estado"]
        labels = {
            "mascota": "Paciente",
            "fecha": "Fecha",
            "hora": "Hora",
            "motivo": "Motivo de la consulta",
            "estado": "Estado",
        }
        widgets = {
            "mascota": forms.Select(attrs={"class": "form-control"}),
            "fecha": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "hora": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "motivo": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Ej.: Revisión general, vacunación, dolor abdominal..."}),
            "estado": forms.Select(attrs={"class": "form-control"}),
        }


class RecepcionistaLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Usuario"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Contraseña"}))
