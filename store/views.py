from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from store.models import Book, Buty

# Create your views here.
from store.serializer import UserSerializer


def index(request):
    buty_list = Buty.objects.all()
    return render(request, 'store.html', {'Buty': buty_list})


def books(request):
    book_count = Book.objects.all().count()
    book_list = Book.objects.all()
    return render(request,
                  'books.html',
                  {'book_count': book_count,
                   'book_list': book_list}
                  )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = UserSerializer
