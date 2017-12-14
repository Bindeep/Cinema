from .serializers import MovieSerializer, GenreSerializer
from cinema.models import Movie, Genre
from rest_framework import viewsets


class GenreViewSet(viewsets.ModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer