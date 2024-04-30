from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

#! ViewSet Classes
from rest_framework.viewsets import ModelViewSet

class TodoMVS(ModelViewSet):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer
    