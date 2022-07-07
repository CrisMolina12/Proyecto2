from dataclasses import fields
import imp
from pyexpat import model
from django import forms
from .models import Producto, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields ='__all__'
    
class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields ='__all__'



class CustomUserCreationForm(UserCreationForm):   
    class Meta:
        model=User
        fields=['username', "first_name","last_name", "email","password1","password2"]