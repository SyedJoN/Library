from . import views
from django.urls import path
from django.contrib.auth.views import LoginView as auth_login, LogoutView as auth_logout

urlpatterns =[
    path('signup', views.signup, name='signup'),
    path('login', auth_login.as_view(template_name='Users/login.html'), name='login'),
    path('logout', auth_logout.as_view(template_name='Users/logout.html'), name='logout'),
    path('<str:user_name>/favorites', views.favorites, name='favorites'),
    path("<str:user_name>/<int:book_id>/added", views.addToFav, name='addToFav'),
    path('<str:user_name>/<int:book_id>/removed', views.remFromFav, name='remFromFav'),
    path("<str:user_name>/issued", views.issuedBooks, name='issuedBooks'),
    path("<int:book_id>/<str:user_name>/added", views.addToIssued, name='addToIssued'),
    path('<str:user_name><int:book_id>', views.remFromIssued, name='remFromIssued'),
    ]