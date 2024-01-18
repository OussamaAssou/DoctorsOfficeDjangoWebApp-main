from django.db import models
from datetime import datetime
# Create your models here.

# Modèle pour représenter un patient
class Paciente(models.Model):
    # Identifiant du patient
    id = models.PositiveIntegerField(primary_key=True, null=False)
    
    # Liste des types d'identité avec leurs codes et libellés
    lista_tipo = [('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte'), ('PE', 'Permiso de Permanencia'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad')]
    
    # Champ pour le type d'identité du patient
    tipo_id = models.CharField(max_length=2, null=True, choices=lista_tipo)
    
    # Champ pour le prénom du patient
    nombres = models.CharField(max_length=64, null=False)
    
    # Champ pour le nom de famille du patient
    apellidos = models.CharField(max_length=64, null=False)
    
    # Champ pour l'adresse du patient
    direccion = models.CharField(max_length=64, null=True)
    
    # Champ pour les numéros de téléphone du patient
    telefonos = models.CharField(max_length=20, null=True)
    
    # Champ pour l'adresse e-mail du patient
    email = models.EmailField(max_length=254, null=True)
    
    # Champ pour le mot de passe du patient
    password = models.CharField(max_length=8, null=False)

    # Méthode spéciale pour représenter le patient en tant que chaîne de caractères
    def __str__(self):
        return f"{self.nombres} - {self.apellidos}"

# Modèle pour représenter un médecin
class Medico(models.Model):
    # Identifiant du médecin
    id = models.PositiveIntegerField(primary_key=True, null=False)
    
    # Champ pour le prénom du médecin
    nombres = models.CharField(max_length=64, null=False)
    
    # Champ pour le nom de famille du médecin
    apellidos = models.CharField(max_length=64, null=False)
    
    # Champ pour l'adresse du médecin
    direccion = models.CharField(max_length=64, null=True)
    
    # Champ pour les numéros de téléphone du médecin
    telefonos = models.CharField(max_length=20, null=True)
    
    # Champ pour l'adresse e-mail du médecin
    email = models.EmailField(max_length=254, null=True)
    
    # Champ pour la spécialité du médecin
    especialidad = models.CharField(max_length=64, null=True)
    
    # Champ pour le mot de passe du médecin
    password = models.CharField(max_length=8, null=False)

    # Méthode spéciale pour représenter le médecin en tant que chaîne de caractères
    def __str__(self):
        return f"{self.nombres} - {self.apellidos}"

# Modèle pour représenter une heure de rendez-vous
class CitaHora(models.Model):
    # Identifiant de l'heure de rendez-vous
    id = models.AutoField(primary_key=True, null=False)
    
    # Champ pour l'heure du rendez-vous, avec la valeur par défaut définie à l'heure actuelle
    hora = models.TimeField(default=datetime.now().time(), null=False)

    # Méthode spéciale pour représenter l'heure de rendez-vous en tant que chaîne de caractères
    def __str__(self):
        return f"{self.id} => {self.hora}"

# Modèle pour représenter un rendez-vous entre un médecin et un patient
class Cita(models.Model):
    # Identifiant du rendez-vous
    id = models.AutoField(primary_key=True, null=False)
    
    # Clé étrangère liée à un objet Medico (médecin)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=False)
    
    # Clé étrangère liée à un objet Paciente (patient)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False)
    
    # Clé étrangère liée à un objet CitaHora (heure de rendez-vous)
    hora = models.ForeignKey(CitaHora, on_delete=models.CASCADE, null=False)
    
    # Champ pour la date du rendez-vous, avec la valeur par défaut définie à la date actuelle
    fecha = models.DateField(default=datetime.now().date(), null=False)
    
    # Liste de choix pour le champ cancelada, avec des options "Si" (Oui) et "No" (Non)
    lista_cancela = [('S', 'Si'), ('N', 'No')]
    
    # Champ pour indiquer si le rendez-vous a été annulé, avec des choix limités à la liste définie
    cancelada = models.CharField(max_length=1, null=False, choices=lista_cancela, default='N', blank=False)
    
    # Champ pour stocker l'heure d'annulation du rendez-vous, avec la valeur par défaut à l'heure actuelle
    hora_cancelada = models.TimeField(default=datetime.now().time(), blank=False)

    # Méthode spéciale pour représenter le rendez-vous en tant que chaîne de caractères
    def __str__(self):
        return f"{self.paciente} => {self.medico} => {self.fecha} => {self.hora}"
