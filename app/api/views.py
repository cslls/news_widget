from api import serializers
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import News 
from api.serializers import NewsSerializer

class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

@api_view(['GET'])
def getNews(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addNews(request):
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
