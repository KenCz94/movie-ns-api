from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie, Genre, Score, WatchList
from .serializer import MovieSerializer, GenreSerializer, ScoreSerializer, WatchListSerializer
from .pagination import DefaultResultsSetPagination
from django.db.models import Avg

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.annotate(score_filter=Avg('score__score')).all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    pagination_class = DefaultResultsSetPagination
    filter_backends = (OrderingFilter,)
    ordering_fields = ('title', 'created_by', 'release_date', 'score_filter')

class WatchListViewSet(viewsets.ModelViewSet):
    queryset = WatchList.objects.all().order_by('-create_date')
    serializer_class = WatchListSerializer
    http_method_names = ['get', 'post', 'delete', 'head']
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'movie']

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all().order_by('-create_date')
    serializer_class = ScoreSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'movie']

