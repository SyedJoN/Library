from . import views
from django.urls import path
from django.contrib.auth.views import LoginView as auth_login, LogoutView as auth_logout

urlpatterns =[
    path('signup', views.signup, name='signup'),
    path('login', auth_login.as_view(template_name='Users/login.html'), name='login'),
    path('logout', auth_logout.as_view(template_name='Users/logout.html'), name='logout'),
    path('<str:user_name>', views.favorites, name='favorites')
]