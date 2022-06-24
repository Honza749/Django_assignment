import json

from django.core.exceptions import SuspiciousOperation
from rest_framework.decorators import api_view
from rest_framework.response import Response

with open("test_data.json", "r") as file:
    data_input = json.load(file)
data: list = data_input

    
def Merge(dict_1, dict_2):
    """Merge 2 dictionaries"""

    result = dict_1 | dict_2
    return result


def is_valid_json(input_json):
    """Control, if data format is json"""

    try:
        json.loads(input_json)
    except ValueError as e:
        return False
    return True


@api_view(["GET"])
def get_all_data(request):
    """Returns all object available"""
    
    return Response(data)


@api_view(["GET"])
def get_by_name_id(request, model_name, object_id):
    """Returns object with specific name and id"""
 
    for x in data:
        if model_name in x.keys():
            if x[model_name]["id"] == int(object_id):
                return Response(x[model_name])


@api_view(["GET"])
def get_by_name(request, model_name):
    """Return all objects with specific name"""

    output = []
    for x in data:
        if model_name in x.keys():
            output.append(x)
    return Response(output)


@api_view(["POST"])
def process_import(request):
    """Import data"""

    body_unicode = request.body.decode("utf-8")
    if not is_valid_json(body_unicode):
        raise SuspiciousOperation("Invalid request; wrong data posted!")
    body: list = json.loads(body_unicode)
    data.append(body)
    return Response(str("OK"))
