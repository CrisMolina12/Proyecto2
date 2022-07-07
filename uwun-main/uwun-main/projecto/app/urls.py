from django.urls import path
from .views import home, quienessomos, verproducto, productos, adm, carrito, history, inicioadm, iniciosesion, publicar, pagar, perfil, registro, subscripcion

urlpatterns = [
    path('', home, name="home"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('verproducto/', verproducto, name="verproducto"),
    path('productos/', productos, name="productos"),
    path('adm/', adm, name="adm"),
    path('carrito/', carrito, name="carrito"),
    path('history/', history, name="history"),
    path('inicioadm/', inicioadm, name="inicioadm"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('publicar/', publicar, name="publicar"),
    path('pagar/', pagar, name="pagar"),
    path('perfil/', perfil, name="perfil"),
    path('subscripcion/', subscripcion, name="subscripcion"),
    path('registro/', registro, name="registro"),

]
