from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
from django.shortcuts import render

# Create your views here.
