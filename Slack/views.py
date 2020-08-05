# coding: utf-8

import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def listen(request):
    data = json.loads(request.body)
    print(data)
    return JsonResponse({})