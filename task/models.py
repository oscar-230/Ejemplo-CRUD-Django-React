from django.db import models

# Create your models here.
class Task (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    done = models.BooleanField(default=False)
    
    #que dato queremos ver al momento que lo estamos ejecutando en el administrador
    def __str__(self):
        return self.title
    