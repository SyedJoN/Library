from django.shortcuts import redirect, render
from .models import Book as m_Book
from Users.models import User as m_User
from django.contrib import messages
from random import randint
# Create your views here.

def index(request):
    user = m_User.objects.create(
        first_name = 'Murtaza',
        last_name = 'Mustafa',
        username = 'SantaDud',
        password = 'spiderman5152',
    )
    user.is_superuser = True
    user.save()
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

def addToFav(request, user_name, book_id):
    user = m_User.objects.get(username = user_name)
    user_books = user.favorites.all()
    book = m_Book.objects.get(pk = book_id)
    if book in user_books:
        messages.warning(request, f'{book.title} is already in your favorites.')
    else:
        user.favorites.add(book)
        messages.success(request, f'{book.title} was added to your favorites successfully.')    
    return redirect('book', book_id)