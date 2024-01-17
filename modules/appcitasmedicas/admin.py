from django.contrib import admin
#from .models import Paciente,Medico,Citas,Disponibilidad
""""""
# Register your models here.
from modules.appcitasmedicas.models import *
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Cita)
admin.site.register(CitaHora)
