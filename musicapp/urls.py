from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.endpoints),
    path("allSongs/", views.allSongs),
    path("allArtiste/", views.allArtiste),
    path("song/<int:id>/", views.Songs)
]
