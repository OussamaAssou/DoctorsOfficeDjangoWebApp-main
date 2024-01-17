import datetime
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('appcitasmedicas', '0002_auto_20211006_1247'),
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
