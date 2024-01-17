import datetime
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('appcitasmedicas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now().date()),
        ),
        migrations.AlterField(
            model_name='cita',
            name='hora_cancelada',
            field=models.TimeField(default=datetime.datetime.now().time()),
        ),
        migrations.AlterField(
            model_name='citahora',
            name='hora',
            field=models.TimeField(default=datetime.datetime.now().time()),
        ),
    ]
