from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from modules.appcitasmedicas.models import Paciente


class PacienteBackEnd(ModelBackend):

    def authenticate(self, request, **kwargs):
        try:
            usuario = request.POST["username"]
            password = request.POST["password"]

            paciente = Paciente.objects.get(id=usuario, password=password)
            
            return paciente
        

        except ObjectDoesNotExist:
            None