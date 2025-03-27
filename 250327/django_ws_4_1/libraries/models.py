from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()
    isbn = models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    salespoint = models.IntegerField()
    customerrating = models.IntegerField()

    