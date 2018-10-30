from rest_framework import serializers
from .models import Track, PlayList

class TrackSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    year = serializers.IntegerField()

class PlaylistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        return PlayList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()

        return instance

class PlayListContentSerializer(serializers.Serializer):
    playlist = serializers.IntegerField()
    track = serializers.IntegerField()

    def update(self, instance, validated_data):
        record = PlayList.objects.get(pk=validated_data['playlist'])
        instance.playlist.add(record)
        instance.save()
        return instance
