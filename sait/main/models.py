from django.db import models

class Tovar(models.Model):
    nazv = models.CharField(max_length=50)
    opis = models.TextField()
    chena = models.IntegerField()
