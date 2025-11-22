from django.db import models
import uuid
from apps.Productivity_Tracker.models.project import Project
from apps.Productivity_Tracker.models.category import Category

class Tasks(models.Model):
    class Priority(models.TextChoices):
        HIGH = 'H', 'High'
        MEDIUM = 'M', 'Medium'
        LOW = 'L', 'Low'
        
    class Status(models.TextChoices):
        COMPLETED = 'C', 'COMPLETED'
        INPROGRESS = 'I', 'INPROGRESS'
        NOTSTARTED = 'N', 'NOTSTARTED'
         
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)
    priority = models.CharField(
        max_length=1,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    status = models.CharField(
        max_length=1,
        choices=Status,
        default=Status.NOTSTARTED
        )
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.title} ({self.get_priority_display()})"