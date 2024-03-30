# NOTA: Archivo creado manualmente
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from task import views

router = routers.DefaultRouter()
router.register(r'task', views.TaskView, 'task')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="task API"))
]

# Todo este codigo esta generando las rutas GET, POST, PUT, DELETE