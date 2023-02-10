from dataclasses import field
from msilib.schema import CheckBox
from pyexpat import model
from django import forms
from django.forms import ModelForm, fields, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pkg_resources import require
from .models import Presupuesto

# class presupuestoForm(ModelForm):
#     class Meta:
#         model = Presupuesto
#         fields = ['nombreCliente', 'telefonoCliente', 'correoCliente', 'direccionCliente', 'descripcionPresupuesto']

class presupuestoForm(Form):
    nombreCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'col-sm-12 col-md-11', 'placeholder':'Nombre'}), label="")
    telefonoCliente = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'col-sm-12 col-md-11', 'placeholder':'Telefono'}), label="")
    correoCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'col-sm-12 col-md-11','placeholder':'Correo Electrónico'}), label="")
    direccionCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'col-sm-12 col-md-11','placeholder':'Dirección'}), label="")
    descripcionPresupuesto = forms.CharField(widget=forms.Textarea(attrs={'class':'col-sm-12 col-md-12', 'placeholder':'Descripción', 'rows':'15', 'cols':'20'}), label="")

class presupuestoSoloForm(Form):
    nombreCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'col-sm-12 col-md-6', 'placeholder':'Nombre'}), label="")
    telefonoCliente = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'col-sm-12 col-md-6', 'placeholder':'Telefono'}), label="")
    correoCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'col-sm-12 col-md-6','placeholder':'Correo Electrónico'}), label="")
    direccionCliente = forms.CharField(widget=forms.TextInput(attrs={'class':'col-sm-12 col-md-6','placeholder':'Dirección'}), label="")
    descripcionPresupuesto = forms.CharField(widget=forms.Textarea(attrs={'class':'col-sm-12 col-md-12', 'placeholder':'Descripción', 'rows':'15', 'cols':'20'}), label="")


class iniciar_sesionForm(Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'pad-textbox centerHor col-sm-12 col-lg-12 form-control'}), label="Correo")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'pad-textbox centerHor col-sm-12 col-lg-12 form-control'}), label="Contraseña")
    class Meta:
        fields = ['username', 'password'] 

# class EditarUsuario(Form):
#     first_name = forms.CharField(max_length=150,required=True,label="Nombres")
#     last_name = forms.CharField(max_length=150, required=True, label="Apellidos")
#     email = forms.CharField(max_length=254, required=True, label="Correo")
#     rutUsuario = forms.CharField(max_length=12, required=True, label="Rut")
#     direccion = forms.CharField(max_length=300, required=True, label="Direccion")
#     esSuscriptor = forms.BooleanField(required=False,label="Tener suscripción")
#     imagen = forms.ImageField(label="Imagen Usuario", required=False)
#     class Meta:
#         fields = '__all__'