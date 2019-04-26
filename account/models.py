from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    verify_password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Login(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name