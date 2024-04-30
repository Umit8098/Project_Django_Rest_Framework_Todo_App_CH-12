from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = (  # normalde list içinde ama böyle de olur.
            'id',
            'task',
            'description',
            'priority',
            'is_done',
            'created_date',
        )
