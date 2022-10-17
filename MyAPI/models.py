from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)

    def __str__(self):
        return self.name + "," + self.genre
