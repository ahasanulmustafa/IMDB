from django.contrib import admin
from .models import Profile, Media, Cast, Movie, Genre, RatingsAndComments


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'password', 'date_of_birth', 'age', 'country']


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'videos', 'images']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'poster', 'release_date', 'Media', 'genre', 'is_released']


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'movie']


@admin.register(RatingsAndComments)
class RatingsAndCommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'movie']
