from django.shortcuts import render
from django.views.generic import *
from .models import Tasks
from .forms import TaskForm
from django.urls import reverse_lazy

# Create your views here.

class TaskCreateView(CreateView):
    model = Tasks
    template_name = "CreateTask.html"
    fields = "__all__"
    success_url = reverse_lazy("listTask")

class TaskListView(ListView):
    model = Tasks
    template_name = "ListTask.html"
    context_object_name = "tasks"

class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = "DeleteTask.html"
    success_url = reverse_lazy("listTask")

class TaskUpdateView(UpdateView):
    model = Tasks
    template_name = "UpdateTask.html"
    fields = "__all__"
    form = TaskForm
    success_url = reverse_lazy("listTask")

class TaskDetailView(DetailView):
    model = Tasks
    template_name='ViewTask.html'
    form = TaskForm
    context_object_name = 'task'