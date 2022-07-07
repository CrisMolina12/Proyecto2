from email import message
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def quienessomos(request):
    return render(request, 'app/quienessomos.html')

def verproducto(request):
    return render(request, 'app/verproducto.html')

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)


def adm(request):
    return render(request, 'app/adm.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def history(request):
    return render(request, 'app/history.html')

def inicioadm(request):
    return render(request, 'app/inicioadm.html')

def iniciosesion(request):
    return render(request, 'app/iniciosesion.html')

def pagar(request):
    return render(request, 'app/pagar.html')

def perfil(request):
    return render(request, 'app/perfil.html')

def publicar(request):
    data ={
        'form': ProductoForm()
    }

    if request.method == 'POST':
        data = {
            'form': ProductoForm()
        }

        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "Producto publicado"
            else:
                data["form"] = formulario
    return render(request, 'app/publicar.html', data)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleanned_data["password1"])
            login(request, user)
            
            #se va al home
            return redirect(to="home")
    return render(request, 'registration/registro.html', data)

def subscripcion(request):
    return render(request, 'app/subscripcion.html')

