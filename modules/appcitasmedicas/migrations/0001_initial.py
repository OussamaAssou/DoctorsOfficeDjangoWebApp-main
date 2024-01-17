import datetime
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitaHora',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hora', models.TimeField(default=datetime.datetime.now().time())),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=64)),
                ('apellidos', models.CharField(max_length=64)),
                ('direccion', models.CharField(max_length=64, null=True)),
                ('telefonos', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('especialidad', models.CharField(max_length=64, null=True)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('tipo_id', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PA', 'Pasaporte'), ('PE', 'Permiso de Permanencia'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad')], max_length=2, null=True)),
                ('nombres', models.CharField(max_length=64)),
                ('apellidos', models.CharField(max_length=64)),
                ('direccion', models.CharField(max_length=64, null=True)),
                ('telefonos', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=datetime.datetime.now().date())),
                ('cancelada', models.CharField(choices=[('S', 'Si'), ('N', 'No')], default='N', max_length=1)),
                ('hora_cancelada', models.TimeField(default=datetime.datetime.now().time())),
                ('hora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcitasmedicas.citahora')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcitasmedicas.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcitasmedicas.paciente')),
            ],
        ),
    ]
