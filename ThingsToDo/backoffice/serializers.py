from rest_framework import serializers
from .models import Task, Subtask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("name", "description", "priority", "start_date", "end_date", "place")
    
class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ("name", "description", "order")
    
