from django.db import models

class Task(models.Model):
  content = models.CharField(max_length=500)
  isImportent = models.BooleanField(default=False, null=True)
  isCompleted = models.BooleanField(default=False, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.content