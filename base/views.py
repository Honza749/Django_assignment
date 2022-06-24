import json

from django.core.exceptions import SuspiciousOperation
from rest_framework.decorators import api_view
from rest_framework.response import Response

with open("test_data.json", "r") as file:
    data_input = json.load(file)

data: list = data_input
print(type(data))


@api_view(["GET"])
def get_all_data(request):
    return Response(data)


@api_view(["GET"])
def get_by_name_id(request, model_name, object_id):
    print(model_name)
    for x in data:
        if model_name in x.keys():
            if x[model_name]["id"] == int(object_id):
                return Response(x[model_name])


@api_view(["GET"])
def get_by_name(request, model_name):
    output = []
    for x in data:
        if model_name in x.keys():
            print(type(x))
            output.append(x)
    return Response(output)


def Merge(dict_1, dict_2):
    result = dict_1 | dict_2
    return result


def is_valid_json(input_json):
    try:
        json.loads(input_json)
    except ValueError as e:
        return False
    return True


@api_view(["POST"])
def process_import(request):
    print(request)
    body_unicode = request.body.decode("utf-8")
    if not is_valid_json(body_unicode):
        raise SuspiciousOperation("Invalid request; wrong data posted!")
    body: list = json.loads(body_unicode)
    data.append(body)
    return Response(str("OK"))
