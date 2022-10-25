from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from musicapp.models import Song, Artiste, Lyric
from musicapp.serializers import SongSerializer, ArtisteSerializer, LyricSerializer

# get list of artists
@api_view(['GET', 'POST'])
def artiste_list(request):
    if request.method == 'GET':
        artists = Artiste.objects.all()
        serializer = ArtisteSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View for getting, updating and deleting an individual Artist
@api_view(['GET', 'PUT', 'DELETE'])
def artiste_details(request, pk):
    try:
        artist = Artiste.objects.get(pk=pk)
    except Artiste.DoesNotExist:
        return Response(status=status.HTTp_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtisteSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ArtisteSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get list of songs
@api_view(['GET', 'POST'])
def song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View for getting, updating and deleting an individual Song
@api_view(['GET', 'PUT', 'DELETE'])
def song_details(request, pk):
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

