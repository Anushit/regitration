from .models import artist
from .serializers import ArtistSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .forms import *

@api_view(['GET','POST'])
def index(request):
    print(request.user)
    print(request.auth)
    if request.method == "GET":
        return Response(data={"message":"Welcome to Home"},status=status.HTTP_200_OK)
    elif request.method == "POST":
        return Response(data=request.data,status=status.HTTP_200_OK)
    else:
        return Response(data="Request Method Invaild")

@api_view(['GET'])
def artistList(request):
    art = artist.objects.all()
    serializer = ArtistSerializer(art,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artistdetail(request,pk):
    art = artist.objects.get(id=pk)
    serializer = ArtistSerializer(art,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def artistCreate(request):
    serializer = ArtistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def artistUpdate(request,pk):
    art = artist.objects.get(id=pk)
    serializer = ArtistSerializer(instance=art, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def artistDelete(request,pk):
    art = artist.objects.get(id=pk)
    art.delete()
    return Response('Deleted')

