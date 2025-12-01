#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linebook.settings')
django.setup()

from nucleo.models import Libro

# Crear libros de prueba
Libro.objects.create(
    titulo="El Alquimista",
    imagen="https://via.placeholder.com/200x300?text=El+Alquimista",
    sinopsis="Una novela sobre un joven que busca su destino."
)

Libro.objects.create(
    titulo="Cien años de soledad",
    imagen="https://via.placeholder.com/200x300?text=Cien+anos",
    sinopsis="La historia de la familia Buendía a lo largo de generaciones."
)

Libro.objects.create(
    titulo="1984",
    imagen="https://via.placeholder.com/200x300?text=1984",
    sinopsis="Una distopía donde el totalitarismo controla la sociedad."
)

Libro.objects.create(
    titulo="Harry Potter y la Piedra Filosofal",
    imagen="https://via.placeholder.com/200x300?text=Harry+Potter",
    sinopsis="Un joven mago descubre su verdadera identidad."
)

print("✓ 4 libros creados exitosamente")
print("IDs disponibles para buscar: 1, 2, 3, 4")
