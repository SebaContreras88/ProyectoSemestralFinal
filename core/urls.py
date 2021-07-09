from django.urls import path
from .views import index
from .views import iniciosesion
from .views import registrarse
from .views import contacto
from .views import manualidades
from .views import pinturas
from .views import orfebreria
from .views import tejidos
from .views import listaArtes
from .views import NuevaArte
from .views import editarArte
from .views import eliminarArte

urlpatterns = [
    path('',index,name='index'),
    path('iniciosesion/',iniciosesion,name='iniciosesion'),
    path('registrarse/',registrarse,name='registrarse'),
    path('contacto/',contacto,name='contacto'),
    path('manualidades/',manualidades,name='manualidades'),
    path('orfebreria/',orfebreria,name='orfebreria'),
    path('tejidos/',tejidos,name="tejidos"),
    path('pinturas/',pinturas,name='pinturas'),
    path('listaArtes/',listaArtes,name='listaArtes'),
    path('listaArtes/AgregarArte',NuevaArte,name='nuevaArte'),
    path('listaArtes/editarArte/<id>',editarArte,name='editarArte'),
    path('listaArtes/eliminarArte/<id>',eliminarArte,name='eliminarArte'),
]