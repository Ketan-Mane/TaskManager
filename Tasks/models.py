from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date = models.DateField()
    status = models.BooleanField(default=False)
    class Meta:
        db_table = "tasks"