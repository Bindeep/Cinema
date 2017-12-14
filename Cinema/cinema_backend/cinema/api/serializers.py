from rest_framework import serializers
from cinema.models import Movie, Genre, Tag

# class GenreSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Genre
# 		fields = '__all__'


# class MovieSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Movie
# 		exclude = ('poster',)


class GenreSerializer(serializers.ModelSerializer):
	movies = serializers.StringRelatedField(many=True)
	class Meta:
		model = Genre
		fields = ('name', 'movies')



class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		exclude = ('poster',)