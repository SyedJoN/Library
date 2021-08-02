from django.db import models
from django.db.models import BooleanField, CharField, TextField, ForeignKey
from django.db.models.fields import DateField
from django.db.models.fields.files import FileField, ImageField
from django.core.files.storage import FileSystemStorage
# Create your models here.

fileStorage = FileSystemStorage(location='Books/')

class Book(models.Model):
    title = CharField(max_length=50)
    author = CharField(max_length=30)
    cover = ImageField(storage=fileStorage, upload_to='static/Books/')
    description = TextField()
    ISBN = CharField(max_length=14)
    bookPDF = FileField(storage=fileStorage, upload_to='static/Books/')
    isIssued = BooleanField(default=False)
    issuedTo = ForeignKey(to='Users.User', related_name="issuedBooks", on_delete=models.PROTECT, null=True)
    dateIssued = DateField(auto_now=True, null=True)
    dateReturned = DateField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


