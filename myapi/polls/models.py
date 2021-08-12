from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Partfolio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    loyixa_nomi = models.CharField(max_length=200)
    malumot = models.TextField()
    startdate = models.DateField()
    finishdate = models.DateField()

    def __str__(self):
        return self.loyixa_nomi
