from django.db import models

# Create your models here.


class Rating(models.Model):
    rating = models.IntegerField()
    timestamp = models.IntegerField()


class Movie(models.Model):
    movieid = models.IntegerField()
    rating = models.ForeignKey(Rating)


class Rater(models.Model):
    rater = models.IntegerField()
    movie = models.ForeignKey(Movie)
