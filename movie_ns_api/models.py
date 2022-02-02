from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Add a movie genre')

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)    
    description = models.TextField(null=True, blank=True)
    produced_by = models.CharField(max_length=100, blank=True)
    release_date = models.IntegerField(null=True, blank=True)
    fandango_url = models.CharField(max_length=255, null=True, blank=True)
    poster_url = models.URLField(max_length=255, null=True, blank=True)
    created_by = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre')

    @property
    def average(self):
        return Score.objects.filter(movie=self).aggregate(avg=models.Avg('score'))['avg'] or 0
    
class WatchList(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.CharField(max_length=255, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('movie', 'user',)

class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)    

    class Meta:
        unique_together = ('movie', 'user',)

