from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ns/api/', include('movie_ns_api.urls')),
]