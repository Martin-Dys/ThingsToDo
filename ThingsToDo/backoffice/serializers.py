from rest_framework import serializers
from .models import Task, Subtask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("name", "description", "priority", "start_date", "end_date", "place")

        def update(self, instance, validated_data):
            instance.name = validated_data.get("name", instance.name)
            instance.description = validated_data.get("description", instance.description)
            instance.save()
            return instance
    
class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ("name", "description", "order")
    
