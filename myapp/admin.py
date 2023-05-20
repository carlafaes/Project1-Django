from django.contrib import admin
from .models import Project,Task

# Agrega modelos al panel de administrador
admin.site.register(Project)
admin.site.register(Task)
