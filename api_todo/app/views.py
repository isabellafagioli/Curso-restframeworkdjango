from rest_framework import serializers
from app.models import Todo
from app.serializers import TodoSerializer
from app.serializers import TodoSerializer
from rest_framework import generics


class TodoListAndCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer