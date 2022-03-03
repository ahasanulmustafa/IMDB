from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=50)


class Media(models.Model):
    videos = models.FileField(upload_to=None, max_length=50)
    images = models.ImageField()


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    poster = models.ImageField()
    release_date = models.DateTimeField()
    Media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='media')
    genre = models.ManyToManyField(Genre, related_name='genre', blank=True)
    is_released = models.BooleanField(default=True)

    def get_genre(self):
        return "\n".join([g.name for g in self.genre.all()])

    def __str__(self):
        return self.title


class Cast(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


rate_choices = [
    (1, '1-Trash'),
    (2, '2- Horrible'),
    (3, '3- Terrible'),
    (4, '4- Bad'),
    (5, '5- OK'),
    (6, '6- Watchable'),
    (7, '7- Good'),
    (8, '8- Very Good'),
    (9, '9- Perfect'),
    (10, '10- Master Piece'),
]


class RatingsAndComments(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=rate_choices, blank=True)
