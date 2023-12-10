from django.db import models

# Create your models here.

class Participante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)

class Curso(models.Model):
    descripcion = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    participantes = models.ManyToManyField(Participante)

class Tutor_IA(models.Model):
    gpt = models.CharField(max_length=255)
    key = models.CharField(max_length=255)

class Tutor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    especialidades = models.CharField(max_length=30)
    #FK
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, blank=True)

class Documento(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=30)
    formato = models.CharField(max_length=30)
    #FK
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, blank=True)
