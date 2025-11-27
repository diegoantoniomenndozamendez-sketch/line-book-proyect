from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("libro/<int:id>/", views.detalle_libro, name="detalle_libro"),
    path("libro/<int:id>/", views.detalle_libro, name="detalle_libro"),

]
