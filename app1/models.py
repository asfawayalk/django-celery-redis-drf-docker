from operator import mod
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=555)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)