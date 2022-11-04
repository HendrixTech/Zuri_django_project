from rest_framework import serializers

from .models import Song, Artiste, Lyric

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "date_released",
            "likes",
            "artiste_id",
        )
        model = Song

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "first_name",
            "last_name",
            "age",
        )
        model = Artiste

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            "content",
        )
        model = Lyric