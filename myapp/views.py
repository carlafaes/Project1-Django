from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request):
    return HttpResponse("Task")