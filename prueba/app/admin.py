from django.contrib import admin

from app.views import publicar
from .models import Categoria,Producto,Usuario,Publicar

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Publicar)
admin.site.register(Usuario)



