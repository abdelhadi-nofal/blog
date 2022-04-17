from django.shortcuts import render
from django.http import JsonResponse
from .blog import blog
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Artical

from .serializers import ArticalSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(req):
    return Response('This is Blog BackEnd to go to database api/blog')

@api_view(['GET'])
def getBlog(req):
    articals = Artical.objects.all()
    serializer = ArticalSerializer(articals, many= True)
    return Response(serializer.data)


@api_view(['GET'])
def getArtical(req,pk):
    artical = Artical.objects.get(id=pk)
    serializer = ArticalSerializer(artical, many= False)
    return Response(serializer.data)