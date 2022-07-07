from django.urls import path
from .views import admmodificar, index, adm, carrito,historial, inicioadm, iniciosesion, pagar, perfil, productos, publicar, quienessomos, registro, subcripcion, verproducto, admproducto, admmodificar,eliminarproducto, eliminarusuario, modificarusuario, registro, verProducto

urlpatterns = [
    path('home',index, name="home" ),
    path('adm/',adm, name="adm" ),
    path('carrito/',carrito, name="carrito" ),
    path('historial/',historial, name="historial" ),
    path('inicioadm/',inicioadm, name="inicioadm" ),
    path('iniciosesion/',iniciosesion, name="iniciosesion" ),
    path('pagar/',pagar, name="pagar" ),
    path('perfil/',perfil, name="perfil" ),
    path('productos/',productos, name="productos" ),
    path('publicar/',publicar, name="publicar" ),
    path('quienessomos/',quienessomos, name="quienes" ),
    path('registro/',registro, name="regis" ),
    path('subscripcion/',subcripcion, name="subscripcion" ),
    path('verproducto/',verproducto, name="verproducto" ),
    path('admproductos/',admproducto, name="admproducto" ),
    path('modificarproducto/<id>',admmodificar, name="admmodificar" ),
    path('eliminaproducto/<id>',eliminarproducto, name="eliminaproducto" ),
    path('eliminarusuario/<id>',eliminarusuario, name="eliminarusuario" ),
    path('modificauser/<id>',modificarusuario, name="modificarusuario" ),
    path('registro/',registro, name="registro" ),
    path('verProducto/<id>', verProducto, name="verProducto"),
    
    
    
    
]