from django.shortcuts import render
from .models import Book as m_Book
from random import randint
# Create your views here.

def index(request):
    numberOfBooks = m_Book.objects.count()
    first = m_Book.objects.first().pk
    bookIds = []
    for i in range(3):
        temp = randint(first, numberOfBooks + first - 1)
        while(temp in bookIds):
            temp = randint(first, numberOfBooks + first - 1)
        bookIds.append(temp)
    return render(request, 'Books/index.html', {
        "books": m_Book.objects.all(),
        "rBook1": m_Book.objects.get(pk = int(bookIds[1])),
        "rBook2": m_Book.objects.get(pk = int(bookIds[0])),
        "rBook3": m_Book.objects.get(pk = int(bookIds[2])),
    })

def book(request, book_id):
    return render(request, 'Books/book.html', {
        "book": m_Book.objects.get(pk = book_id)
    })

def search(request):
    searchText = request.GET['searchText']
    return render(request, 'Books/search.html', {
        "books": m_Book.objects.filter(title__icontains = searchText)
    })
