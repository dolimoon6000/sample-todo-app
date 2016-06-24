from rest_framework import serializers

from .models import ToDoItem


class ToDoItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)

    class Meta:
        model = ToDoItem
