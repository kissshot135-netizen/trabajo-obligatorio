from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import CitaForm, MascotaForm, RecepcionistaLoginForm
from .models import Cita, Mascota


def login_recepcionista(request):
    if request.method == 'POST':
        form = RecepcionistaLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenido/a, {user.username}.')
            return redirect('agenda_diaria')
    else:
        form = RecepcionistaLoginForm()
    return render(request, 'clinica/login.html', {'form': form})


@login_required(login_url='login_recepcionista')
def logout_recepcionista(request):
    logout(request)
    return redirect('login_recepcionista')


@login_required(login_url='login_recepcionista')
def agenda_diaria(request):
    citas = Cita.objects.select_related('mascota').filter(fecha=datetime.today().date())
    total = Cita.objects.count()
    pendientes = Cita.objects.filter(estado='pendiente').count()
    atendidas = Cita.objects.filter(estado='atendida').count()
    return render(
        request,
        'clinica/agenda_diaria.html',
        {'citas': citas, 'total': total, 'pendientes': pendientes, 'atendidas': atendidas}
    )


@login_required(login_url='login_recepcionista')
def nueva_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente registrado correctamente.')
            return redirect('agenda_diaria')
    else:
        form = MascotaForm()
    return render(request, 'clinica/nueva_mascota.html', {'form': form})


@login_required(login_url='login_recepcionista')
def nueva_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita creada correctamente.')
            return redirect('agenda_diaria')
    else:
        form = CitaForm()
    return render(request, 'clinica/form_cita.html', {'form': form, 'titulo': 'Nueva cita'})


@login_required(login_url='login_recepcionista')
def editar_cita(request, cita_id):
    cita = Cita.objects.get(pk=cita_id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita actualizada correctamente.')
            return redirect('agenda_diaria')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'clinica/form_cita.html', {'form': form, 'titulo': 'Editar cita'})


@login_required(login_url='login_recepcionista')
def eliminar_cita(request, cita_id):
    cita = Cita.objects.get(pk=cita_id)
    if request.method == 'POST':
        cita.delete()
        messages.success(request, 'Cita eliminada correctamente.')
        return redirect('agenda_diaria')
    return render(request, 'clinica/eliminar_cita.html', {'cita': cita})


@login_required(login_url='login_recepcionista')
def listar_citas(request):
    citas = Cita.objects.select_related('mascota').all()
    return render(request, 'clinica/listar_citas.html', {'citas': citas})
