# Prompts para IA - Clínica Huellas Sanas

## 1) Generar HTML/CSS responsivo para formulario y tabla

Prompt:

> Actúa como desarrollador frontend senior en Django. Necesito una interfaz web responsive para una clínica veterinaria llamada "Huellas Sanas". Genera un formulario para registrar una nueva mascota con estos campos: nombre, especie, raza y nombre del dueño. También genera una tabla para mostrar la agenda diaria de citas con columnas: mascota, dueño, fecha, hora, motivo y estado. Usa un diseño moderno, limpio y de tonos verdes/terra. Debe verse bien en desktop y mobile. Devuélveme el código HTML/CSS listo para integrar en templates de Django, sin dependencias externas.

## 2) Generar datos ficticios para pruebas

Prompt:

> Eres un experto en Python y Django. Crea un script de gestión para generar 20 pacientes y 20 citas ficticias para una clínica veterinaria. Usa nombres de mascotas, dueños, especies, razas, motivos y estados aleatorios. Inserta los datos en la base con los modelos Mascota y Cita de Django. El script debe evitar duplicados y ejecutarse con `python manage.py seed_data`.

## 3) Gestionar citas mediante Django

Prompt:

> Implementa un sistema de gestión de citas para una clínica veterinaria con Django. Debes crear modelos `Mascota` y `Cita`, registrar los modelos en el admin, crear vistas para listar la agenda diaria y registrar nuevas mascotas, y configurar URLs para que un recepcionista use el sistema. Añade validaciones básicas, filtros por fecha y estado, y utiliza SQLite para pruebas.
