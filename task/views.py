from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer # Para que traiga la clase que ya tengo creada en serializer.py
    queryset = Task.objects.all() # para traer todas las tareas de models.py
    