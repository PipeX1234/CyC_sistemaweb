from django.shortcuts import render, redirect
from asyncio.windows_events import NULL
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from .forms import iniciar_sesionForm, presupuestoForm
from .models import Presupuesto
import requests
# Create your views here.

def mostrar_index(request):

    data={"form":presupuestoForm, "mesg":""}
    if(request.method == "POST"):
        form = presupuestoForm(request.POST)
        if (form.is_valid()):
            try:
                idPresupuesto = Presupuesto.objects.all().count() + 1
                nombreCliente = request.POST.get("nombreCliente")
                telefonoCliente = request.POST.get("telefonoCliente")
                correoCliente = request.POST.get("correoCliente")
                direccionCliente = request.POST.get("direccionCliente")
                descripcionPresupuesto = request.POST.get("descripcionPresupuesto")
                Presupuesto.objects.create(nombreCliente = nombreCliente, telefonoCliente = telefonoCliente, correoCliente=correoCliente, direccionCliente=direccionCliente, descripcionPresupuesto = descripcionPresupuesto)
                try:
                    tele_auth_token = os.environ.get('API_key')
                    tel_group_id = os.environ.get('teleID')
                    msg=f"Cliente: {nombreCliente}\nContacto Telefono: {telefonoCliente}\nContacto Correo: {correoCliente}\nDirección: {direccionCliente}\n\nDescripción del caso:\n{descripcionPresupuesto}"
                    telegram_api_url=f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id=@{tel_group_id}&text={msg}"
                    tel_resp = requests.get(telegram_api_url)

                    if tel_resp.status_code==200:
                        print("Se ha enviado correctamente el mensaje")
                    else:
                        print("No se ha logrado enviar el mensaje")
                        raise Exception('No se ha logrado enviar el mensaje')

                except:
                    print("Ha ocurrido un error al enviar a Telegram")
                data["mesg"] = "Se ha enviado correctamente"
            except:
                data["mesg"] = "Ha ocurrido un error, por favor, intentelo nuevamente más tarde"


    return render(request, "core/index.html", data)

def mostrar_ventajas(request):
    return render(request, 'core/ventajas.html')

def mostrar_trabajos(request):
    return render(request, 'core/trabajos.html')

def mostrar_servicios(request):
    return render(request, 'core/servicios.html')

def mostrar_presupuesto(request):
    data={"form":presupuestoForm, "mesg":""}
    if(request.method == "POST"):
        form = presupuestoForm(request.POST)
        if (form.is_valid()):
            try:
                nombreCliente = request.POST.get("nombreCliente")
                telefonoCliente = request.POST.get("telefonoCliente")
                correoCliente = request.POST.get("correoCliente")
                direccionCliente = request.POST.get("direccionCliente")
                descripcionPresupuesto = request.POST.get("descripcionPresupuesto")
                Presupuesto.objects.create(nombreCliente = nombreCliente, telefonoCliente = telefonoCliente, correoCliente=correoCliente, direccionCliente=direccionCliente, descripcionPresupuesto = descripcionPresupuesto)
                try:
                    tele_auth_token = "6134014021:AAFNbkWgs0WXoKITQWQuYPNMQHJBu1tDEow"
                    tel_group_id = "testinTeleP"
                    msg=f"Cliente: {nombreCliente}\nContacto Telefono: {telefonoCliente}\nContacto Correo: {correoCliente}\nDirección: {direccionCliente}\n\nDescripción del caso:\n{descripcionPresupuesto}"
                    telegram_api_url=f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id=@{tel_group_id}&text={msg}"
                    tel_resp = requests.get(telegram_api_url)

                    if tel_resp.status_code==200:
                        print("Se ha enviado correctamente el mensaje")
                    else:
                        print("No se ha logrado enviar el mensaje")
                        raise Exception('No se ha logrado enviar el mensaje')

                except:
                    print("Ha ocurrido un error al enviar a Telegram")
                data["mesg"] = "Se ha enviado correctamente"
            except:
                data["mesg"] = "Ha ocurrido un error, por favor, intentelo nuevamente más tarde"

    return render(request, 'core/presupuesto.html', data)

def iniciar_sesion(request):
    data = {"form": iniciar_sesionForm, "mesg":""}
    if request.method == "POST": 
        form = iniciar_sesionForm(request.POST)
        if form.is_valid:
            print('Es valido')
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active and user.is_staff:
                    login(request, user)
                    return redirect(mostrar_presupuesto_admin, action='e')
                else:
                    data["mesg"] = "Su usuario o contraseña no son correctos"
            else:
                data["mesg"] = "Su usuario o contraseña no son correctos"

    return render(request, 'core/inicio-sesion.html', data)

def cerrar_sesion(request):
    logout(request)
    return redirect(mostrar_index)

def mostrar_presupuesto_admin(request, action):
    if( not request.user.is_authenticated or not request.user.is_staff ):
        return redirect(mostrar_index)
    
    data = {"list": "", "mesg":""}

    if(action == "e"):
        try:
            list = Presupuesto.objects.all().order_by('-idPresupuesto')
        except:
            data["mesg"] = "Ha ocurrido un error, intentelo nuevamente más tarde"

    elif(action == "b"):
        try:
            nomBusc = request.GET.get('nomBusc')
            list = Presupuesto.objects.filter(nombreCliente__icontains = nomBusc).order_by('-idPresupuesto', 'nombreCliente')
        except:
            data["mesg"] = "Ha ocurrido un error, intentelo nuevamente más tarde"

    if(len(list) < 1 ):
        data["mesg"] = "No se han encontrado presupuestos actualmente"
    else:
        data["list"] = list
    
    
    return render(request, 'core/presupuesto-admin.html', data)