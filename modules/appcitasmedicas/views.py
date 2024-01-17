from typing import ContextManager
from modules.appcitasmedicas.models import *
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

# Create your views here.
def home(request):

    try:
        del request.session['id_paciente']
    except KeyError:
        pass

    return render(request, 'home.html')

def autenticar(request):

    #Authenticate user
    try:
        if request.method == "POST":
            usuario = request.POST["username"]
            password = request.POST["password"]

            paciente = Paciente.objects.get(id=usuario, password=password)
        
            context = {"paciente" : paciente}
            request.session['id_paciente'] = paciente.id
    

    except ObjectDoesNotExist:
        context = {"mensaje" : "Paciente y/o contraseña inválidos."}
        return render(request, 'login.html', context)    

    return render(request, 'usuario.html', context)

def logout(request):

    try:
        del request.session['id_paciente']
    except KeyError:
        pass

    return render(request, 'home.html')
    
def login(request):

    return render(request, 'login.html')

def usuario(request):
    paciente = Paciente.objects.get(id= request.session['id_paciente'])

    context = {"paciente":paciente}

    return render(request, 'usuario.html', context)

def agendamiento(request):
    paciente = Paciente.objects.get(id= request.session['id_paciente'])

    context = {"paciente":paciente}
    return render(request, 'agendamiento.html', context)

def medicos(request):
    medicos = Medico.objects.all().order_by('apellidos')

    return JsonResponse(list(medicos.values('id', 'apellidos', 'nombres')), safe = False)
    
def consultas(request):
    citas = Cita.objects.filter(paciente= request.session['id_paciente'], cancelada = 'N').order_by('-id') # creo el querySet 
    #[::-1]
    paciente = Paciente.objects.get(id= request.session['id_paciente'])
    #cita_paciente = Cita.objects.fil.all() () # creo el querySet 
    context = {"citas":citas,"paciente":paciente} # Creo el contexto para pasarlo a la pagina
    return render(request, 'consultas.html', context)

def cancelar(request, id):
    citas=Cita.objects.get(id=id)
    citas.cancelada='S'
    citas.save()
    return redirect('consultas')

def horas(request):
    citas = Cita.objects.filter(medico= request.POST['idmedico'], fecha= request.POST['fechacita'], cancelada = 'N').values('hora')
    horas = CitaHora.objects.all().exclude(id__in=citas).order_by('hora')

    return JsonResponse(list(horas.values('id', 'hora')), safe = False)

def cita(request):
    if request.method == "POST":
        cita = Cita()
        cita.medico = Medico.objects.get(id=request.POST['idmedico'])
        cita.paciente = Paciente.objects.get(id=request.POST['idpaciente'])
        cita.hora = CitaHora.objects.get(id=request.POST['hora'])
        cita.fecha = request.POST['fechacita']
        cita.save()

    return redirect('consultas')