from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()
    
class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Examen(models.Model):
    embarcacion = models.CharField(max_length=10)
    profe_examinador = models.CharField(max_length=30)
    fecha_examen = models.DateField()
    aprobado = models.BooleanField()



