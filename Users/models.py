from django.contrib.auth.models import AbstractUser as django_User
from django.db.models import ManyToManyField
from Books.models import Book
# Create your models here.

class User(django_User):
    favorites = ManyToManyField(Book)
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'