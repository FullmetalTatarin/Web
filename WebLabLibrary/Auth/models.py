from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=25)
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    role = models.IntegerField()
