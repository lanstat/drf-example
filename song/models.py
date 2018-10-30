from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PlayList(models.Model):
    name = models.CharField(max_length=50)

class Track(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    year = models.SmallIntegerField(default=0)
    playlist = models.ManyToManyField(PlayList, blank=True)

    def __str__(self):
        return self.name