from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Item
from .serializers import ItemSerializer
from django.contrib.auth.models import User

@shared_task
def create_item(name, created_by):
    item = Item.objects.create(name=name, created_by_id=created_by)
    serialized = ItemSerializer(item).data
    print(".........................item created.......................")
    print(serialized)
    print(".........................item created.......................")

