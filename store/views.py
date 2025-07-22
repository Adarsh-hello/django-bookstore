from django.shortcuts import render # type: ignore
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})
