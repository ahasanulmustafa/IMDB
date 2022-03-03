from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profilelist/', views.ProfileListCreate.as_view()),
    path('profilelist/<int:pk>', views.ProfileRetrieveUpdateDestroy.as_view()),
    path('movielist/', views.MovieListCreate.as_view()),
    path('movielist/<int:pk>', views.MovieRetrieveUpdateDestroy.as_view()),
    path('castlist/', views.CastListCreate.as_view()),
    path('castlist/<int:pk>', views.CastRetrieveUpdateDestroy.as_view()),
    path('castmovie/<int:pk>', views.CastMovieListApi.as_view()),
    path('castupcoming/<int:pk>', views.CastUpcomingMovieApi.as_view()),

]
