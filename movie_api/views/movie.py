"""View module for handling requests about movies"""
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from movie_api.models import Movie


class MovieView(ViewSet):
    def list(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def create(self, request):
        movie = Movie.objects.create(
            title=request.data['title'],
            year=request.data['year'],
            genre_id=request.data['genre_id']
        )

        movie.actors.set(request.data['actors'])

        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.title = request.data['title']
        movie.year = request.data['year']
        movie.genre_id = request.data['genre_id']

        movie.actors.set(request.data['actors'])
        movie.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'genre', 'actors')
        depth = 1
