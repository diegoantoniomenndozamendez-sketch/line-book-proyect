from django.core.management.base import BaseCommand
from nucleo.models import Libro


class Command(BaseCommand):
    help = "Crea libros de prueba en la base de datos"

    def handle(self, *args, **options):
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

        self.stdout.write(self.style.SUCCESS("✓ 4 libros creados exitosamente"))
        self.stdout.write(self.style.SUCCESS("IDs disponibles para buscar: 1, 2, 3, 4"))
