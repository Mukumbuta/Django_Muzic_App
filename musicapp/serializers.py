from rest_framework import serializers
from musicapp.models import Song, Artiste, Lyrics


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['first_name', 'last_name', 'age']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['artiste_id', 'title', 'date_released', 'likes']


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = ['song_id', 'content']