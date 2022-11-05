from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Artiste, Song
from .serializers import ArtisteSerializer, SongSerializer
# Create your views here.


@api_view(['GET'])
def endpoints(request):
    endpoints = {
        'all songs' : '/allSongs/',
        'all artiste' : '/allArtiste/',
        'manipulate_song': '/song/<int:id>/'
    }

    return Response(endpoints)


@api_view(['GET'])
def allSongs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def allArtiste(request):
    artiste = Artiste.objects.all()
    serializer = ArtisteSerializer(artiste, many=True)

    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def Songs(request, id):
    if request.method == 'GET':
        song = Song.objects.get(id=id)
        serializer = SongSerializer(song, many=False)

        return Response(serializer.data)

    
    if request.method == 'DELETE':
        song = Song.objects.get(id=id)
        song.delete()

        return Response("Song deleted")

    
    if request.method == "PUT":
        song = Song.objects.get(id=id)
        serializer = SongSerializer(instance=song, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response("Song updated!")