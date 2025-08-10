from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # ✅ Restrict access

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # ✅ Restrict access