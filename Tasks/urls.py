from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(),name="listTask"),
    path('addtask', TaskCreateView.as_view(),name="createTask"),
    path('viewtask/<int:pk>', TaskDetailView.as_view(),name="viewTask"),
    path('updatetask/<int:pk>', TaskUpdateView.as_view(),name="updateTask"),
    path('deletetask/<int:pk>', TaskDeleteView.as_view(),name="deleteTask"),
]
