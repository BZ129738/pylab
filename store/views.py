from django.shortcuts import render
from django.http import HttpResponse
from store.models import Book

# Create your views here.

def index(request):
    return render(request,'store.html')


def books(request):
    book_count = Book.objects.all().count()
    book_list = Book.objects.all()
    return render(request,
                  'books.html',
                  {'book_count': book_count,
                  'book_list': book_list}
                  )
