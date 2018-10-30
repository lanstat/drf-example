from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Track, PlayList
from .serializers import TrackSerializer, PlayListContentSerializer, PlaylistSerializer
from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics

class PlaylistList(generics.ListAPIView):
    """
    Lista todas las canciones guardadas
    """

    def get(self, request, format=None):
        records = PlayList.objects.all()
        serializer = PlaylistSerializer(records, many =True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = PlaylistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrackList(generics.ListAPIView):
    """
    Lista todas las canciones guardadas
    """
    serializer_class = TrackSerializer

    def get_queryset(self):
        queryset = Track.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__contains=name)

        year = self.request.query_params.get('year', None)
        if year is not None:
            queryset = queryset.filter(year=year)

        return queryset

class TrackDetail(APIView):
    def get_object(self, pk):
        try:
            record = Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            return Http404
        return record

    def get(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = TrackSerializer(record)
        return Response(serializer.data)

class PlaylistDetail(APIView):
    def get_object(self, pk):
        try:
            record = PlayList.objects.get(pk=pk)
        except PlayList.DoesNotExist:
            return Http404
        return record

    def get(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = PlaylistSerializer(record)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        record = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = PlaylistSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        record = self.get_object(pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistContentList(APIView):
    def get(self, request, pk, format=None):
        records = Track.objects.filter(playlist=pk)
        serializer = TrackSerializer(records, many=True)
        return Response(serializer.data)

class PlaylistContentDetail(APIView):
    def get_object(self, pk):
        try:
            record = Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            return Http404
        return record

    def post(self, request, pk, trackPk, format=None):
        record = self.get_object(trackPk)
        data = {"playlist": pk, "track": trackPk}
        serializer = PlayListContentSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, trackPk, format=None):
        record = self.get_object(trackPk)
        playlist = PlayList.objects.get(pk=pk)
        record.playlist.remove(playlist)
        record.save()
        return Response(status=status.HTTP_204_NO_CONTENT)