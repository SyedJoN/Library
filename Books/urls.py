from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name='index'),
    path("<int:book_id>", views.book, name='book'),
    path("search", views.search, name='search'),
    path("<str:user_name><int:book_id>/added", views.addToFav, name='addToFav'),
]
