from blog.model.blog_managment_model import BlogManagment
from django.http import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Blog
from django.core import serializers
from django.utils import timezone

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")


def users_list(request):
    data = [
        {'name': "Sehal", 'email': 'seinsehal@gmail.com'},
        {'name': "Sein", 'email': 'sehal@redintegro.com'}
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def insert_user(request):
    data = json.loads(request.body.decode('utf-8'))
    return JsonResponse(data, safe=False)

def user_detail(request, id):
    data = {'name': "Sehal", 'email': 'seinsehal@gmail.com', 'id': id}
    return JsonResponse(data)


def blog_list(request):
    data = Blog.objects.all()
    response = serializers.serialize("json", data)
    return HttpResponse(response, content_type="application/json")

@csrf_exempt
@require_http_methods(['POST'])
def insert_blog(request):
    data = json.loads(request.body.decode('utf-8'))

    # if data['name'] == None:
    #     print("Error")

    BlogManagment.get_list_of_profiles()
    return JsonResponse(data)



@csrf_exempt
@require_http_methods(['POST'])
def update_blog(request,id):
    data = json.loads(request.body.decode('utf-8'))

    old_blog = Blog.objects.get(pk=id)

    old_blog.description = data['description']
    old_blog.name = data['name']
    old_blog.save()
    
    return JsonResponse(data)

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_blog(request,id):
    old_blog = Blog.objects.get(pk=id)
    old_blog.delete()
    
    return HttpResponse("Record Deleted")

# CRUD
# Create new model
# Fetch list of data
# Insert Data to DB
# Updated Data; model.save()
# Deleting Data; model.delete()