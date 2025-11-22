from django.db import models
import uuid
from apps.Productivity_Tracker.models.tasks import Tasks


class Deadlines(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)