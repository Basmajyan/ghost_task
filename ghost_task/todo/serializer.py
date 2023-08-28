from rest_framework import serializers
from todo.models import Todo, Status

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        extra_kwargs = {
            'spent': {'format': '%Y-%m-%d %H:%M:%S'}
        }

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
