from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ["created_by", "id", "created_at", "updated_at"]
    
    def create(self, validated_data):
        validated_data["created_by"] = self.context.get("request").user
        return super(ItemSerializer, self).create(validated_data)

class ItemLightSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=555)

