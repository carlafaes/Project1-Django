from django.urls import path
from myapp import views ##Se importan las vistas de la carpeta myapp


urlpatterns=[
    path('',views.hello),
    path('about/',views.about),
    path('projects/',views.projects),
    path('tasks/<int:id>',views.tasks),
]