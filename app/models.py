from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	email = models.EmailField()
	fecha = models.DateField()

	def __str__(self):
		return self.nombre

