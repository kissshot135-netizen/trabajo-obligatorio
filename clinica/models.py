from django.db import models


class Mascota(models.Model):
    ESPECIE_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Conejo', 'Conejo'),
        ('Hamster', 'Hamster'),
        ('Ave', 'Ave'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES)
    raza = models.CharField(max_length=100)
    nombre_dueno = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"


class Cita(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('atendida', 'Atendida'),
        ('cancelada', 'Cancelada'),
    ]

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    class Meta:
        ordering = ['fecha', 'hora']
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'

    def __str__(self):
        return f"{self.mascota.nombre} - {self.fecha} {self.hora}"
