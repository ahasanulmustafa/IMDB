from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Profile, Media, Genre, Movie, Cast, RatingsAndComments
from .serializers import ProfileSerializer, MediaSerializer, GenreSerializer, MovieSerializer, CastSerializer, \
    RatingsAndCommentsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from rest_framework.response import Response


def home(request):
    return HttpResponse("Hello Welcome to the IMDB")


# Profile API

class ProfileListCreate(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# Movie API

class MovieListCreate(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Cast API

class CastListCreate(ListCreateAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


class CastRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer


@permission_classes((permissions.AllowAny,))
class CastMovieListApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            mov = Movie.objects.filter(cast__profile_id=id)
            serializer = MovieSerializer(mov, many=True)
            return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class CastUpcomingMovieApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            mov = Movie.objects.filter(cast__profile_id=id).filter(is_released=False)
            serializer = MovieSerializer(mov, many=True)
            return Response(serializer.data)


