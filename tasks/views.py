from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "create_task.html", {"form": form})


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "task_detail.html", {"task": task})


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)

    return render(request, "edit_task.html", {"form": form})


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect("task_list")


def delete_confirmation(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "delete_task.html", {"task": task})
