from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def data(request):
    return HttpResponse("Data page")


def page(request):
    return HttpResponse("My page")


def myname(request):
    imie = 'Bartosz'
    nazwisko = 'Zabinski'
    indeks = 129738
    return render(request,
                  'myname.html',
                  {'imie': imie,
                   'nazwisko': nazwisko,
                   'indeks': indeks})
