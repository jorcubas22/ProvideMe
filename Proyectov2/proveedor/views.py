from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import proveedor
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView

@login_required
def home(request):
    context = {
        'proveedor' : proveedor.objects.select_related('provincia')
    }
    return render(request, 'proveedor/proveedor.html', context)

class proveedorListView(ListView):
    model = proveedor
    template_name = 'proveedor/proveedor.html'
    context_object_name = 'proveedor'
    ordering = ['-nombre']

class ProvDetailView(DetailView):
    model = proveedor

class ProvCreateView(CreateView):
    model = proveedor
    fields = ['nombre', 'correo', 'telefono', 'provincia']

def search(request):
    template = 'proveedor/proveedor.html'
    query = request.GET.get('q')
    if query:
        results = proveedor.objects.filter(Q(nombre__icontains=query))
    else:
        results = proveedor.objects.filter(status='published')
    pages = pagination(request, result, num=1)

    context = {
        'items':pages[0],
        'page_range': pages[1],
    }
    return render(request, template, context)