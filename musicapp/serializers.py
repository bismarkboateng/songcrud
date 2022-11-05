from rest_framework import serializers
from .models import Artiste, Song

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste 
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"