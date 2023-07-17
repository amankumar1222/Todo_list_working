
from django.urls import path , include
from .import views


urlpatterns = [
    path('', views.index, name="home" ),
    path('task/', views.task, name="task" ),
    path('edit/<int:id>/', views.edit, name="edit" ),
    path('delete/<int:id>/', views.deleteTask, name="edit" ),
]

