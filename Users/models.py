from django.contrib.auth.models import AbstractUser as django_User
from django.db.models import ManyToManyField
from django.db.models.fields import IntegerField
# Create your models here.

class User(django_User):
    favorites = ManyToManyField(to='Books.Book')
    fine = IntegerField(default=0)
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'