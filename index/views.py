from django.shortcuts import render
from rest_framework import generics
from .serializers import *

from .models import *

# Create your views here.

class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserialzers

class TodoDetail(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserialzers

class TodoCreate(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserialzers

class TodoDelete(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserialzers
