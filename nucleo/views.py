from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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


def agregar_libro(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        imagen = request.POST.get("imagen", "").strip()
        sinopsis = request.POST.get("sinopsis", "").strip()

        if not titulo or not imagen or not sinopsis:
            messages.error(request, "Por favor completa todos los campos.")
            return render(request, "nucleo/agregar_libro.html")

        try:
            Libro.objects.create(titulo=titulo, imagen=imagen, sinopsis=sinopsis)
            messages.success(request, f"¡Libro '{titulo}' agregado exitosamente!")
            return redirect("buscar_libro")
        except Exception as e:
            messages.error(request, f"Error al agregar el libro: {str(e)}")

    return render(request, "nucleo/agregar_libro.html")


def buscar_libro(request):
    query = request.GET.get("q", "").strip()
    libros = []

    if query:
        if query.isdigit():
            libros = Libro.objects.filter(id=int(query))
        else:
            libros = Libro.objects.filter(titulo__icontains=query)
    else:
        libros = Libro.objects.all()

    return render(request, "nucleo/buscar_libro.html", {
        "libros": libros,
        "query": query,
    })


def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        imagen = request.POST.get("imagen", "").strip()
        sinopsis = request.POST.get("sinopsis", "").strip()

        if not titulo or not imagen or not sinopsis:
            messages.error(request, "Por favor completa todos los campos.")
            return render(request, "nucleo/editar_libro.html", {"libro": libro})

        try:
            libro.titulo = titulo
            libro.imagen = imagen
            libro.sinopsis = sinopsis
            libro.save()
            messages.success(request, f"¡Libro '{titulo}' actualizado exitosamente!")
            return redirect("buscar_libro")
        except Exception as e:
            messages.error(request, f"Error al actualizar el libro: {str(e)}")

    return render(request, "nucleo/editar_libro.html", {"libro": libro})


def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    
    if request.method == "POST":
        titulo = libro.titulo
        libro.delete()
        messages.success(request, f"¡Libro '{titulo}' eliminado exitosamente!")
        return redirect("buscar_libro")

    return render(request, "nucleo/confirmar_eliminar.html", {"libro": libro})

