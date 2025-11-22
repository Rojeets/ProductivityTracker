from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Goals(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.ForeignKey(AbstractUser, null=False, on_delete=models.CASCADE)
    