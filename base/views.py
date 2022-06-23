from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item


@api_view(['GET'])
def getIns(request):
    api_urls = {
        'List': '/task-list/',
        'Details': '/task-detail/<str:pk>/'
    }
    return Response(api_urls)
#

@api_view(['GET'])
def allData(request):
    tasks = Item.objects.all()
    serializer = ItemSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail_by_id(nazev_modelu, pk):
    tasks = Item.objects.get(id=pk)
    serializer = ItemSerializer(tasks, many=False)
    return Response(serializer.data)

#+ funkce filtr podle  jmena


@api_view(['POST'])
def addData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
    task = Item.objects.get(id=pk)
    task.delete()
    return("Item succesfully deleted")

