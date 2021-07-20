from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    description = models.TextField()
    nationality = models.CharField(max_length=100)
    image = models.FilePathField(path='/players/img')
