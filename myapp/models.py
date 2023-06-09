from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name## retorno los nombres en la url admin

class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    project=models.ForeignKey(Project, on_delete=models.CASCADE)##se eliminan valores de la clase Task, si se borra su clase Project

    def __str__(self):
        return self.title+" - "+self.project.name