from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Item
from .serializers import ItemSerializer
from django.contrib.auth.models import User
import time

@shared_task
def create_item(name, created_by):
    time.sleep(5)
    item = Item.objects.create(name=name, created_by_id=created_by)
    serialized = ItemSerializer(item).data
    print(".........................item created.......................")
    print(serialized)
    print(".........................item created.......................")
    return "item creation done"

@shared_task
def debug_task():
    for i in range(5):
        print(i, "celery is working")
    return "Done"