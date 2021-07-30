from django.core.files import storage
from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import FileField, ImageField
from django.core.files.storage import FileSystemStorage
# Create your models here.

fileStorage = FileSystemStorage(location='Books/')

class Book(models.Model):
    title = CharField(max_length=50)
    author = CharField(max_length=30)
    cover = ImageField(storage=fileStorage, upload_to='static/Books/pictures')
    description = TextField()
    ISBN = CharField(max_length=14)
    bookPDF = FileField(storage=fileStorage, upload_to='static/Books/pdf')
    
    def __str__(self):
        return f"{self.title} by {self.author}"


