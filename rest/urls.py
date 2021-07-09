from django.urls import path
from .views import detalle_arte, lista_artes
from .viewslogin import login

urlpatterns = [
    path('arte/listar', lista_artes, name='lista_artes'),
    path('arte/listar/detalle/<id>', detalle_arte, name='detalle_arte'),
    path('login',login,name='login')
]