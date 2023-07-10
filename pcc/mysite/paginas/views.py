from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'templates/index.html')

def teste(request):
    return HttpResponse("Estpu fazendo um teste!")