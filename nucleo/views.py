from django.shortcuts import render, get_object_or_404
from .models import Libro

def inicio(request):
    query = request.GET.get("q")

    if query:
        # Si la búsqueda es numérica, asumimos que el usuario busca por ID exacto
        if query.isdigit():
            libros_recomendados = Libro.objects.filter(id=int(query))
        else:
            # Búsqueda por título (contiene, case-insensitive)
            libros_recomendados = Libro.objects.filter(titulo__icontains=query)

        # Cuando hay una búsqueda queremos mostrar sólo el/los resultados encontrados
        mas_libros = []
    else:
        libros_recomendados = Libro.objects.all()[:3]
        mas_libros = Libro.objects.all()[3:10]

    return render(request, "nucleo/inicio.html", {
        "query": query,
        "libros_recomendados": libros_recomendados,
        "mas_libros": mas_libros,
    })


def detalle_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    return render(request, "nucleo/detalle_libro.html", {"libro": libro})
