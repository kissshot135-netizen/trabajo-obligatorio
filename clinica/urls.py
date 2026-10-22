from django.urls import path

from . import views

urlpatterns = [
    path("", views.agenda_diaria, name="agenda_diaria"),
    path("login/", views.login_recepcionista, name="login_recepcionista"),
    path("logout/", views.logout_recepcionista, name="logout_recepcionista"),
    path("mascotas/nueva/", views.nueva_mascota, name="nueva_mascota"),
    path("citas/", views.listar_citas, name="listar_citas"),
    path("citas/nueva/", views.nueva_cita, name="nueva_cita"),
    path("citas/<int:cita_id>/editar/", views.editar_cita, name="editar_cita"),
    path("citas/<int:cita_id>/eliminar/", views.eliminar_cita, name="eliminar_cita"),
]
