from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet, ScoreViewSet, WatchListViewSet

router = DefaultRouter()
router.register('movie', MovieViewSet)
router.register('genre', GenreViewSet)
router.register('score', ScoreViewSet)
router.register('watchlist', WatchListViewSet)

urlpatterns = [
    path('', include(router.urls))
]