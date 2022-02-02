from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    actors = models.ManyToManyField("Actor", through="MovieActor")
