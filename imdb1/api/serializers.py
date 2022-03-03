from rest_framework import serializers
from .models import Profile, Media, Cast, Movie, Genre, RatingsAndComments


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'password', 'date_of_birth', 'age', 'country')


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'videos', 'images')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class MovieSerializer(serializers.ModelSerializer):
    media = MediaSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster', 'release_date', 'media', 'genre', 'is_released')


class CastSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Cast
        fields = ('id', 'profile', 'movie')


class RatingsAndCommentsSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = RatingsAndComments
        fields = ('id', 'profile', 'movie')