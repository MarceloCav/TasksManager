from rest_framework import serializers
from .models import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'created_at', 'updated_at']
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True},
            'due_date': {'required': True}
        }

    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("The due date cannot be in the past.")
        return value
