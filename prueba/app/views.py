from dataclasses import dataclass
from email import message
from pyexpat.errors import messages
from django.http import Http404
from django.shortcuts import render,redirect, get_object_or_404
from .models import Producto,Usuario
from .forms import ProductoForm, UsuarioForm, CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def adm(request):
    usuarios = Usuario.objects.all()
    
    data = {
        'usuarios': usuarios
    }
    return render(request,'app/adm.html',data)

def carrito(request):
    return render(request,'app/carrito.html')

def historial(request):
    return render(request,'app/history.html')

def inicioadm(request):
    return render(request,'app/inicioadm.html')

def iniciosesion(request):
    return render(request,'app/iniciosesion.html')

def pagar(request):
    return render(request,'app/pagar.html')

def perfil(request):
    return render(request,'app/perfil.html')

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'app/productos.html',data)

def publicar(request):
    data ={
       'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="producto agregado"
        else:
            data["form"]=formulario
            
    return render(request,'app/publicar.html',data)

def quienessomos(request):
    return render(request,'app/quienessomos.html')

def registro(request):
    return render(request,'app/register.html')

def subcripcion(request):
    return render(request,'app/subscripcion.html')

def verproducto(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request,'app/verproducto.html',data)

def admproducto(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request,'app/admproducto.html',data)

def admmodificar(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="admproducto")
        data["form"] = formulario
    
    return render(request,'app/admmodificar.html',data)

def eliminarproducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="admproducto")


def eliminarusuario(request, id):
    usuarios = get_object_or_404(Usuario, id=id)
    usuarios.delete()
    return redirect(to="adm")


def modificarusuario(request, id):
    
    usuarios = get_object_or_404(Usuario, id=id)
    
    data = {
        'form': UsuarioForm(instance=Usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuarios)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="adm")
        data["form"] = formulario
    
    return render(request,'app/modificarusuario.html',data)

def registro(request):
    data ={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            
            return redirect(to="home")
        
        data["form"]=formulario
    return render(request, 'registration/registro.html',data)

def verProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {"producto": producto}
    return render(request, "app/verProducto.html", data)