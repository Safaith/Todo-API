from rest_framework import serializers

from .models import *

class Todoserialzers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'date', 'complete',)