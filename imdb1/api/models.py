from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Media(models.Model):
    videos = models.FileField(upload_to=None, max_length=50)
    images = models.ImageField()


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    poster = models.ImageField()
    release_date = models.DateTimeField()
    Media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='media')
    genre = models.ManyToManyField(Genre, on_delete=models.CASCADE, related_name='genre', blank=True)
    is_released = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Cast(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class RatingsAndComments(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

