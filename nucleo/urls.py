from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("libro/<int:id>/", views.detalle_libro, name="detalle_libro"),
    path("agregar-libro/", views.agregar_libro, name="agregar_libro"),
    path("buscar-libro/", views.buscar_libro, name="buscar_libro"),
    path("editar-libro/<int:id>/", views.editar_libro, name="editar_libro"),
    path("eliminar-libro/<int:id>/", views.eliminar_libro, name="eliminar_libro"),
]
