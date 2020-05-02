from django.db import models
from mongoengine import *

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=200,blank=True)

class Links_small(models.Model):
    movieId = models.CharField(max_length=20,blank=True)
    imdbId = models.CharField(max_length=20,blank=True)
    tmdbId = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.movieId

class Metadata(models.Model):
    adult = models.CharField(max_length=20,blank=True)
    belongs_to_collection = models.CharField(max_length=2000,blank=True)
    budget = models.CharField(max_length=20,blank=True)
    genres = models.CharField(max_length=2000,blank=True)
    homepage = models.CharField(max_length=200,blank=True)
    idd = models.CharField(max_length=20,blank=True)
    imdb_id = models.CharField(max_length=200,blank=True)
    original_language = models.CharField(max_length=20,blank=True)
    original_title = models.CharField(max_length=200,blank=True)
    overview = models.CharField(max_length=2000,blank=True)
    popularity = models.CharField(max_length=200,blank=True)
    poster_path = models.CharField(max_length=200,blank=True)
    production_companies = models.CharField(max_length=1000,blank=True)
    production_countries = models.CharField(max_length=1000,blank=True)
    release_date = models.CharField(max_length=200,blank=True)
    revenue = models.CharField(max_length=20,blank=True)
    runtime = models.CharField(max_length=20,blank=True)
    spoken_languages = models.CharField(max_length=200,blank=True)
    status = models.CharField(max_length=20,blank=True)
    tagline = models.CharField(max_length=2000,blank=True)
    title = models.CharField(max_length=200,blank=True)
    video = models.CharField(max_length=20,blank=True)
    vote_average = models.CharField(max_length=20,blank=True)
    vote_count = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.title

class Ratings(models.Model):
    userId = models.CharField(max_length=20,blank=True)
    movieId = models.CharField(max_length=20,blank=True)
    rating = models.CharField(max_length=20,blank=True)
    timestamp = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.userID

class Links(models.Model):
    movieId = models.CharField(max_length=20,blank=True)
    imdbId = models.CharField(max_length=20,blank=True)
    tmdbId = models.CharField(max_length=20,blank=True)

class Credits(models.Model):
    cast = models.CharField(max_length=2000,blank=True)
    crew = models.CharField(max_length=2000,blank=True)
    idd = models.CharField(max_length=20,blank=True)

class Keywords(models.Model):
    idd = models.CharField(max_length=20,blank=True)
    keywords = models.CharField(max_length=2000,blank=True)
