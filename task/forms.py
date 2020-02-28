from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ["content", 'isImportent']

# class isCompleted(forms.ModelForm):
#   class Meta:
#     model = Task
#     fields = ['isCompleted']