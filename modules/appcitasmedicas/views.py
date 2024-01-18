from typing import ContextManager
from modules.appcitasmedicas.models import *            # Importer les modèles dans le fichier models.py
from django.shortcuts import render, redirect           # fonctions pour générer les réponses HTTP
from django.core.exceptions import ObjectDoesNotExist   # Exception levée quand la rqt ne revoie rien
from django.http import JsonResponse                    # Retourner des réponses JSON

# Create your views here.
def home(request):                                      # Vue Home affiche la page d'accueil

    try:
        del request.session['id_paciente']              # Supprime la clé ID patient si existe déjà sinon ignore
    except KeyError:
        pass

    return render(request, 'home.html')                 # Retourne la page home

def autenticar(request):                # Gère l'authentification des utilisateurs

    #Authenticate user
    try:
        if request.method == "POST":
            usuario = request.POST["username"]      # Récupère les informations de connexion
            password = request.POST["password"]

            paciente = Paciente.objects.get(id=usuario, password=password) # Récupère un objet Patient correspondant
        
            context = {"paciente" : paciente}
            request.session['id_paciente'] = paciente.id # Stocke l'ID Patient dans la session
    

    except ObjectDoesNotExist:
        context = {"mensaje" : "Paciente y/o contraseña inválidos."} # Message d'erreur - pas de patient existant
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