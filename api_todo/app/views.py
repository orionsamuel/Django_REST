from app.models import Todo
from app.serializers import TodoSerializer

#from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
#from rest_framework.views import APIView

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

