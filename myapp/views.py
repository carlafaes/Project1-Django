from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404 ##devuelve una pagina 404 si el objeto no existe, en lugar de crear una detencion en el servidor

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request,id):
    task=get_object_or_404(Task, id=id)
    return HttpResponse("Task: %s" % task.title)