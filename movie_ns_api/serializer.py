from rest_framework import serializers
from .models import Movie, Genre, Score, WatchList

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    score_avg = serializers.ReadOnlyField(source='average')
    score_filter = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'produced_by', 'description', 'genre', 'release_date', 'fandango_url', 'poster_url', 'score_avg', 'created_by', 'score_filter')
        read_only_fields = ('create_date', 'score_avg')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['genre'] = [genre.name for genre in instance.genre.all()]
        return data

    def create(self, validated_data):
        genre_data = validated_data.pop('genre', [])
        movie = Movie.objects.create(**validated_data)
        for genre in genre_data:
            movie.genre.add(genre)
        return movie

    def update(self, instance, validated_data):
        genre_data = validated_data.pop('genre', [])
        instance.title = validated_data.get('title', instance.title)
        instance.produced_by = validated_data.get('produced_by', instance.produced_by)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.fandango_url = validated_data.get('fandango_url', instance.fandango_url)
        instance.poster_url = validated_data.get('poster_url', instance.poster_url)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.save()
        instance.genre.clear()
        for genre in genre_data:
            instance.genre.add(genre)
        return instance

class ScoreSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source='movie.title')

    class Meta:
        model = Score
        fields = ('id', 'movie', 'movie_title', 'score', 'comment', 'user', 'create_date')        
        read_only_fields = ('movie_title', 'create_date', )

class WatchListSerializer(serializers.ModelSerializer):
    movie_info = MovieSerializer(many=True, read_only=True)  

    class Meta:
        model = WatchList
        fields = ('id', 'movie', 'movie_info', 'user', 'create_date')        
        read_only_fields = ('create_date',  )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['movie_info'] = MovieSerializer(instance.movie).data
        return data