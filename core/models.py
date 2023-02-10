from django.db import models
from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from sre_parse import Verbose
from tabnanny import verbose
from tkinter import CASCADE
from django.forms import IntegerField 
from django.contrib.auth.models import User
# Create your models here.

class Presupuesto(models.Model):
    idPresupuesto = models.AutoField(primary_key=True, verbose_name="ID de Presupuesto")
    nombreCliente = models.CharField(max_length=150, blank=False, null=False, verbose_name="Nombre de la categoría")
    telefonoCliente = models.IntegerField(blank=False, null=False, help_text="914567845", verbose_name="Telefono Cliente")
    correoCliente = models.CharField(max_length=150, blank=False, null=False, verbose_name="Correo Cliente")
    direccionCliente = models.CharField(max_length=300, blank=False, null=False, verbose_name="Dirección")
    descripcionPresupuesto = models.CharField(max_length=500, blank=False, null=False, verbose_name="Descripción")

    def __str__(self):
        return self.idPresupuesto + ' | ' + self.nombreCliente