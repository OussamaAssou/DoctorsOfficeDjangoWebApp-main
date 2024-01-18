from modules.appcitasmedicas.models import *            
from django.shortcuts import render, redirect           
from django.core.exceptions import ObjectDoesNotExist   
from django.http import JsonResponse                    

# Vue pour la page d'accueil
def home(request):                                      
    try:
        del request.session['id_paciente']              
    except KeyError:
        pass
    return render(request, 'home.html')                 

# Vue pour l'authentification des utilisateurs
def autenticar(request):                
    try:
        if request.method == "POST":
            usuario = request.POST["username"]      
            password = request.POST["password"]
            paciente = Paciente.objects.get(id=usuario, password=password) 
            context = {"paciente" : paciente}
            request.session['id_paciente'] = paciente.id 
    except ObjectDoesNotExist:
        context = {"mensaje" : "Identifiant et/ou mot de passe incorrects."}
        return render(request, 'login.html', context)    
    return render(request, 'usuario.html', context)

# Vue pour la déconnexion
def logout(request):
    try:
        del request.session['id_paciente']
    except KeyError:
        pass
    return render(request, 'home.html')
    
# Vue pour la page de connexion
def login(request):
    return render(request, 'login.html')

# Vue pour la page utilisateur
def usuario(request):
    paciente = Paciente.objects.get(id= request.session['id_paciente'])
    context = {"paciente":paciente}
    return render(request, 'usuario.html', context)

# Vue pour la page d'agenda
def agendamiento(request):
    paciente = Paciente.objects.get(id= request.session['id_paciente'])
    context = {"paciente":paciente}
    return render(request, 'agendamiento.html', context)

# Vue pour récupérer la liste des médecins en format JSON
def medicos(request):
    medicos = Medico.objects.all().order_by('apellidos')
    return JsonResponse(list(medicos.values('id', 'apellidos', 'nombres')), safe=False)
    
# Vue pour la page de consultations
def consultas(request):
    citas = Cita.objects.filter(paciente= request.session['id_paciente'], cancelada='N').order_by('-id')
    paciente = Paciente.objects.get(id= request.session['id_paciente'])
    context = {"citas":citas, "paciente":paciente}
    return render(request, 'consultas.html', context)

# Vue pour annuler un rendez-vous
def cancelar(request, id):
    citas = Cita.objects.get(id=id)
    citas.cancelada = 'S'
    citas.save()
    return redirect('consultas')

# Vue pour récupérer la liste des heures disponibles en format JSON
def horas(request):
    citas = Cita.objects.filter(medico=request.POST['idmedico'], fecha=request.POST['fechacita'], cancelada='N').values('hora')
    horas = CitaHora.objects.all().exclude(id__in=citas).order_by('hora')
    return JsonResponse(list(horas.values('id', 'hora')), safe=False)

# Vue pour enregistrer un rendez-vous
def cita(request):
    if request.method == "POST":
        cita = Cita()
        cita.medico = Medico.objects.get(id=request.POST['idmedico'])
        cita.paciente = Paciente.objects.get(id=request.POST['idpaciente'])
        cita.hora = CitaHora.objects.get(id=request.POST['hora'])
        cita.fecha = request.POST['fechacita']
        cita.save()
    return redirect('consultas')
