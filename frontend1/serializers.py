from rest_framework import serializers
from .models import Frontend1

class Frontend1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Frontend1
        fields = ('id', 'title', 'description', 'completed')