from django.urls import path, include

urlpatterns = [
    path('', include('paginas.urls')),
    # Outras rotas podem estar aqui
]