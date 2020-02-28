from django.shortcuts import render, redirect
from django.contrib import messages
from task.models import Task
from task.forms import AddTaskForm
def home(request):
  return render(request, 'home.html')


def tasks(request):
  if request.method == "POST":
    form = AddTaskForm(request.POST or None)
    if form.is_valid():
      form.save()
      messages.success(request, ("Task item added to tasks!"))
      return redirect('tasks')
    else:
      return redirect('tasks')
  else:
    tasks_items = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks_items})

def delete(request, task_id):
  task_item_to_dlt = Task.objects.get(pk=task_id)
  task_item_to_dlt.delete()
  messages.success(request, ("Task deleted!"))
  return redirect('tasks')