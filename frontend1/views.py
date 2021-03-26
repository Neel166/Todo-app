from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Frontend1Serializer
from .models import Frontend1

# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = Frontend1Serializer
    queryset = Frontend1.objects.all()
