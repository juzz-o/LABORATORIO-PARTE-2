from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse('<h1> Bienvenido a la página principal de la app <h1>')
    #return render(request,'home.html')
    return render(request, 'home.html',{'name':'Juan Juzzo Giraldo Restrepo'})
def about(request):
    return HttpResponse('<h1> Esta es la página de about <h1>')
