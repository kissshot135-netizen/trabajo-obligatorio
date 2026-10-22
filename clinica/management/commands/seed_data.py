import random
from datetime import date, time, timedelta

from django.core.management.base import BaseCommand

from clinica.models import Cita, Mascota


class Command(BaseCommand):
    help = "Genera datos de prueba de 20 mascotas y citas para la clínica"

    def handle(self, *args, **options):
        if Mascota.objects.exists():
            self.stdout.write(self.style.WARNING("Ya existen mascotas cargadas. Se omite la generación inicial."))
            return

        nombres_mascotas = [
            "Luna", "Max", "Nala", "Rocky", "Milo", "Coco", "Daisy", "Simba", "Maya", "Loki",
            "Zeus", "Bella", "Charlie", "Lucy", "Oscar", "Mia", "Thor", "Sasha", "Toby", "Cleo",
        ]
        dueños = [
            "Ana García", "Mateo López", "Sofía Ruiz", "Pedro Díaz", "Valentina Torres",
            "Lucía Mendoza", "Javier Silva", "Camila Romero", "Tomás Vega", "Renata Ortiz",
            "Ignacio Castro", "Fernanda Suárez", "Diego Rojas", "Paula Moreno", "Andrés Peña",
            "Carla Flores", "Nicolás Vidal", "Marina Cárdenas", "Esteban Paredes", "Alicia Reyes",
        ]
        motivos = [
            "Chequeo anual", "Vacunación", "Control de alergias", "Dolor abdominal",
            "Revisión por vacunación", "Consulta por heridas", "Control de peso",
            "Problemas digestivos", "Se revisa comportamiento", "Dolor de oído",
            "Control post operatorio", "Examen general", "Consulta por tos",
            "Seguimiento de tratamiento", "Control de pulgas", "Revisión de piel",
        ]
        especies = ["Perro", "Gato", "Conejo", "Hamster", "Ave"]
        razas = {
            "Perro": ["Labrador", "Collie", "Golden Retriever", "Bulldog", "Beagle", "Doberman"],
            "Gato": ["Siames", "Persa", "Criollo", "Bengalí", "Sphynx"],
            "Conejo": ["Mini Lop", "Lionhead", "Holandés"],
            "Hamster": ["Sirio", "Roborovski"],
            "Ave": ["Canario", "Perico"],
        }
        estados = ["pendiente", "atendida", "cancelada"]

        created_pets = []
        for idx in range(20):
            especie = random.choice(especies)
            pet = Mascota.objects.create(
                nombre=nombres_mascotas[idx],
                especie=especie,
                raza=random.choice(razas[especie]),
                nombre_dueno=dueños[idx],
            )
            created_pets.append(pet)

        today = date.today()
        for pet in created_pets:
            cita_date = today + timedelta(days=random.randint(0, 12))
            cita_hour = random.choice([8, 9, 10, 11, 13, 14, 15, 16])
            Cita.objects.create(
                mascota=pet,
                fecha=cita_date,
                hora=time(cita_hour, random.choice([0, 15, 30, 45])),
                motivo=random.choice(motivos),
                estado=random.choice(estados),
            )

        self.stdout.write(
            self.style.SUCCESS(f"Se crearon 20 mascotas y 20 citas de prueba para la clínica.")
        )
