from django.shortcuts import render, get_object_or_404
from .models import Libro

def inicio(request):
    query = request.GET.get("q")

    if query:
        libros_recomendados = Libro.objects.filter(titulo__icontains=query)
        mas_libros = Libro.objects.filter(titulo__icontains=query)
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
