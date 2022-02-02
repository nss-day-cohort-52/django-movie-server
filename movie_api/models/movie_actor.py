from django.db import models

class MovieActor(models.Model):
    actor = models.ForeignKey("Actor", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    

    