import datetime

from django.db.models import F
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from core.models import URLs, Requests
from .serializers import URLSerializer, RequestSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_url(request):
    serializer = URLSerializer(data=request.data)
    # check url counts for user , max is 20
    if URLs.objects.filter(user=request.user).count() >= 20:
        return Response({'error': 'Maximum URL count reached'}, status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
        url = serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_urls(request):
    user_urls = URLs.objects.filter(user=request.user)
    serializer = URLSerializer(user_urls, many=True)
    return Response(serializer.data)


# delete url
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_url(request, pk):
    url = URLs.objects.get(id=pk)
    url.delete()
    return Response('URL deleted', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_alerts(request):
    alerts = URLs.objects.filter(failed_times__gt=F('threshold'), user=request.user)
    serializer = URLSerializer(alerts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def url_stats(request, url_id):
    # check if url belongs to user
    url = URLs.objects.get(id=url_id)
    if url.user != request.user:
        return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
    url = URLs.objects.get(pk=url_id)
    # return last 24 hours requests
    requests = Requests.objects.filter(url=url, created_at__gte=datetime.datetime.now() - datetime.timedelta(days=1))
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data)
