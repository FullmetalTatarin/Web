from django.db import models


class BookModel(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    publisher = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    price = models.IntegerField()
