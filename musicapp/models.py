from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()


    def __str__(self):
        return f"{self.first_name}"


class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField()
    likes = models.CharField(max_length=50)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE) 


    def __str__(self):
        return f"{self.title} - {self.artiste}"



class Lyric(models.Model):
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


    def __str__(self):
        return "Lyric"