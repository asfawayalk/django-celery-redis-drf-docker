from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ItemSerializer, ItemLightSerializer
from rest_framework.filters import SearchFilter
from .filter_backends import NameFilterBackend
from .models import Item
from rest_framework.views import APIView
from .tasks import create_item
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class ItemsViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [SearchFilter, NameFilterBackend]
    search_fields = ["name"]


class CreateItemView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ItemLightSerializer)
    def post(self, request):
        serializer = ItemLightSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        create_item.delay(validated_data.get("name"), request.user.id)
        return Response({"detail": "Your item is being created in the background"})
