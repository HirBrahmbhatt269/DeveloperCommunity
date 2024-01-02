from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.singleproject, name="project"),
    path('without_param/', views.woparam, name="woparam"), # these names come in handy when you want to render a template for a url
    path('create-project/', views.createProject, name= "create-project"),
    path('update-project/<str:pk>/', views.updateProject, name= "update-project"),
    path('delete-project/<str:pk>/', views.deleteProject, name= "delete-project"),
]
