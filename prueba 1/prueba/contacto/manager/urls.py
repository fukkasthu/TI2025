from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_contactos, name='listar_contactos'),
    path('contacto/<int:pk>/', views.detalle_contacto, name='detalle_contacto'),
    path('nuevo/', views.crear_contacto, name='crear_contacto'),
    path('editar/<int:pk>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:pk>/', views.eliminar_contacto, name='eliminar_contacto'),
]
