from django.db import models
import uuid

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    