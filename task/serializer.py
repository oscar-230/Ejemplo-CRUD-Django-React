# NOTA: Archivo creado manualmente
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task #nombre del modelo desde models.py
        #fields = ('id', 'title', 'description', 'done') para traer uno por uno los campos a serializar desde models.py
        fields = '__all__' # traigo todo desde models.py para serializar
        
        