from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()


class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField()
    likes = models.CharField(max_length=50)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE) 



class Lyric(models.Model):
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.SET_NULL)