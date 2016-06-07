from django.contrib import admin

# Register your models here.
from movierating.models import Rating
from movierating.models import Movie
from movierating.models import Rater

admin.site.register(Rating)
admin.site.register(Movie)
admin.site.register(Rater)
