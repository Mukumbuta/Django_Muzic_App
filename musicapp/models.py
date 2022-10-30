from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=50,  blank=False, null=False)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, related_name='song', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='Song title', blank=False, null=False)
    date_released = models.DateTimeField()
    likes = models.IntegerField()
    

    def __str__(self):
        return self.title

class Lyrics(models.Model):
    song_id = models.ForeignKey(Song, related_name='lyrics', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.content
