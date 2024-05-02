from django.shortcuts import render
from .models import Pagina

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')