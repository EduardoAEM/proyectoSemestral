from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'core/home.html')

def quienesSomos (request):
    return render(request, 'core/QuienesSomos.html')

def registro (request):
    return render(request, 'core/registro.html')

def Carrito (request):
    return render(request, 'core/Carrito.html')

def Contacto (request):
    return render(request, 'core/Contacto.html')