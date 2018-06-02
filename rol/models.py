from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.
# Para el registro de empleados se debe contemplar los siguientes datos:
# Nombre completo, dirección, aldea, municipio, celular, DPI, edad, fotografía, género, puesto.

class empleado(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 150)
    direccion = models.CharField(max_length = 200)
    aldea = models.CharField(max_length = 100)
    municipio_choices = (('Comitancillo','Comitancillo'),('San Lorenzo','San Lorenzo'),)
    municipio = models.CharField(max_length = 12, choices = municipio_choices)
    celular = models.CharField(max_length = 15)
    dpi = models.CharField(max_length = 15)
    edad = models.IntegerField()
    fotografia = models.ImageField(upload_to = 'fotografia/empleado/')
    genero_choices = (('M','M'),('F','F'),)
    genero = models.CharField(max_length = 1, choices = genero_choices)
    puesto_choices = (('Administrador','Administrador'),('Registro','Registro'),)
    puesto = models.CharField(max_length = 13)

    def __str__(self):
        return '%s' % (self.nombre)

# Para los afiliados se debe registrar los siguientes datos:
# Nombre completo, dirección, aldea, municipio, celular, DPI, edad, fotografía, género.

class afiliado(models.Model):
    nombre = models.CharField(max_length = 150)
    direccion = models.CharField(max_length = 200)
    aldea = models.CharField(max_length = 100)
    municipio = models.CharField(max_length = 100)
    celular = models.CharField(max_length = 15)
    dpi = models.CharField(max_length = 15)
    edad = models.IntegerField()
    fotografia = models.ImageField(upload_to = 'fotografia/afiliado/')
    genero_choices = (('M','M'),('F','F'),)
    genero = models.CharField(max_length = 1, choices = genero_choices)
    cuota = models.BooleanField()
    # se dara de baja en caso de que migre o muera
    baja = models.BooleanField()

    def __str__(self):
        return '%s' % (self.nombre)

# Para el registro de los afiliados para las jornadas se debe otorgar una boleta con los siguientes datos:
# Empleado quién registró al afiliado o afiliada, fecha de la cita, lugar, hora, número de turno
# además cada afiliado debe dar una cuota de inscripción de Q 10.00. a.
# Al momento de registrar el sistema debe mostrar cuántas veces el afiliado ha sido atendido en jornadas anteriores.

class registro(models.Model):
    day  = timezone.now()
    hour = timezone.now()
    #formatedHour = hour.strftime("%Y/%m/%d %H:%M:%S")
    formatedDay  = day.strftime("%Y/%m/%d")
    formatedHour = hour.strftime("%H:%M:%S")
    employ = models.ForeignKey(empleado, on_delete = models.CASCADE)
    fecha = models.CharField(max_length=50, default=formatedDay)
    hora = models.CharField(max_length=50, default=formatedHour)
    # fecha = models.DateField(auto_now_add = True)
    lugar_choices = (('Comitancillo','Comitancillo'),('San Lorenzo','San Lorenzo'),)
    lugar = models.CharField(max_length = 12, choices = lugar_choices)
    #el numero de turno sera tomado de el id de la tabla registro
    affiliate = models.ForeignKey(afiliado, on_delete = models.CASCADE)

    def __str__(self):
        return '%s' % (self.empleado)

