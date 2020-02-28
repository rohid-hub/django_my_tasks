from django.contrib import admin
from django.urls import path
from .views import home, tasks, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tasks/', tasks, name='tasks'),
    path('delete/<task_id>', delete, name="delete")
]
