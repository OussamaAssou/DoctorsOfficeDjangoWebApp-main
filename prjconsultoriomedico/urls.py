"""prjconsultoriomedico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from modules.appcitasmedicas.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('autenticar/', autenticar, name='autenticar'),
    path('logout/', logout, name='logout'),
    path('login', login, name='login'),
    path('usuario', usuario, name='usuario'),
    path('agendamiento', agendamiento, name='agendamiento'),
    path('horas', horas, name='horas'),
    path('medicos', medicos, name='medicos'),
    path('cita/', cita, name='cita'),
    path('consultas', consultas, name='consultas'),
    path('cancelar/<int:id>/',cancelar,name='cancelar')
]
