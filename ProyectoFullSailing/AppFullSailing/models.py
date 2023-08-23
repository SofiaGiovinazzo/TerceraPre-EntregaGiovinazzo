from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Email: {self.email}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"


class Examen(models.Model):
    embarcacion = models.CharField(max_length=10)
    profe_examinador = models.CharField(max_length=30)
    fecha_examen = models.DateField()

class Avatar(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f'{self.user} - {self.imagen}'
    



