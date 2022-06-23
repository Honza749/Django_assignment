import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render

# from base.models import item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(object_name):
    dict = []
    with open("test_data.json", "r") as file:
        data_input = json.load(file)
    #for x in data_input:
    #    if object_name in x.keys():
    #        dict.add(x)
    #items = item.objects.all()
    #serializer = ItemSerializer(items, many=True)
    #return JsonResponse(data_input,safe=False)
    return Response(data_input)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
