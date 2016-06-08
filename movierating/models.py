from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=30)
    release_date = models.CharField(max_length=15)
    video_release = models.CharField(max_length=20, null=True)
    imbd_link = models.CharField(max_length=120)
    unknown = models.IntegerField(default=0)
    action = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    animation = models.IntegerField(default=0)
    childrens = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    crime = models.IntegerField(default=0)
    documentary = models.IntegerField(default=0)
    drama = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    filmnoir = models.IntegerField(default=0)
    war = models.IntegerField(default=0)
    western = models.IntegerField(default=0)


class Rater(models.Model):
    userid = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zipcode = models.IntegerField()


class Rating(models.Model):
    userid = models.ForeignKey(Rater)
    movieid = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()
