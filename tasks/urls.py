from django.contrib import admin
from django.urls import path
from .views import home, tasks, delete, isCompleted, isImportent, dltCompletedTasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tasks/', tasks, name='tasks'),
    path('delete/<task_id>', delete, name="delete"),
    path('isCompleted/<task_id>', isCompleted, name="isCompleted"),
    path('isImportent/<task_id>', isImportent, name="isImportent"),
    path('tasks/dltCompletedTasks', dltCompletedTasks),
]
