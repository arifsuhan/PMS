import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_protect
from .models import Book

# Create your views here.
def book_list(request):
    response = list(Book.objects.values())
    print(response)
    # status_code = 400
    # content_type = "application/json"
    # return HttpResponse(json.dumps(response), status = status_code, content_type = content_type )
    return JsonResponse(response, safe=False)

# @csrf_protect
@csrf_exempt
def book_create(request):

    context = {}
    print(request.method)
    if request.method == "POST":
        data = json.loads(request.body)
        object = Book.objects.create(name = data['name'], genre= data['genre'])
        context = {'msg': str(object) + 'successfully created!!!'}

    return JsonResponse(context)

@csrf_exempt
def book_update(request):
    context = {}

    if request.method == "POST":
        data = json.loads(request.body)
        obj = Book.objects.get(pk=data['id'])
        obj.name = data['name']
        obj.genre = data['genre']
        obj.save()
        context = {'msg': str(obj) + ' updated!!!'}

    return JsonResponse(context)

@csrf_exempt
def book_delete(request):

    context = {}

    if request.method == "POST":
        data = json.loads(request.body)
        pk_id = data['id']
        instance = Book.objects.get(id=pk_id)
        instance.delete()
        context = {'msg' : str(pk_id) + " successfully deleted!!!"}
    return JsonResponse(context)