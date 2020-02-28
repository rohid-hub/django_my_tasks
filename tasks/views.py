from django.shortcuts import render, redirect
from django.contrib import messages
from task.models import Task
from task.forms import AddTaskForm

def home(request):  
  all_Tasks = Task.objects.filter(isCompleted=False)
  return render(request, 'home.html', {'tasks': all_Tasks})


def tasks(request):
  if request.method == "POST":
    form = AddTaskForm(request.POST or None)
    if form.is_valid():
      form.save()
      messages.success(request, "Task item has been added to Tasks list!")
      return redirect('tasks')
    else:
      return redirect('tasks')
  else:
    all_Tasks = Task.objects.filter(isCompleted=False)
    completed_Tasks = Task.objects.filter(isCompleted=True)
    return render(request, 'tasks/tasks.html', {'tasks': all_Tasks, 'completed_Tasks': completed_Tasks})

def delete(request, task_id):
  task_item_to_dlt = Task.objects.get(pk=task_id)
  task_item_to_dlt.delete()
  messages.warning(request, "Task item has been deleted!")
  return redirect('tasks')


def isCompleted(request, task_id):
  item = Task.objects.get(pk=task_id)
  if item.isCompleted == False:
    item.isCompleted = True
    item.save()
  else:
    item.isCompleted = False
    item.save()
  return redirect('tasks')

def isImportent(request, task_id):
  item = Task.objects.get(pk=task_id)
  if item.isImportent == False:
    item.isImportent = True
    item.save()
  else:
    item.isImportent = False
    item.save()
  return redirect('tasks')

def dltCompletedTasks(request):
  tasks = Task.objects.filter(isCompleted=True)
  for task in tasks:
    task.delete()
  messages.success(request, 'All completed tasks has been deleted!')
  return redirect('tasks')