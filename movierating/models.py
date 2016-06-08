from django.db import models

# Create your models here.


class Movie(models.Model):
    movieid = models.IntegerField(default=0)
    movie_name = models.CharField(max_length=30, default='name')
    release_date = models.CharField(max_length=15, default='date')
    video_release = models.CharField(max_length=20, null=True)
    imbd_link = models.CharField(max_length=100, default="IMD")
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
    userid = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, default="g")
    occupation = models.CharField(max_length=20, default="occupation")
    zipcode = models.CharField(max_length=15, default="zipcode")


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(default=1)
    timestamp = models.IntegerField(default=1)
