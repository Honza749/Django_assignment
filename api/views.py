import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from base.models import item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    with open("test_data.json", "r") as file:
        data_input = json.load(file)
    #items = item.objects.all()
    #serializer = ItemSerializer(items, many=True)
    return Response(data_input)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
