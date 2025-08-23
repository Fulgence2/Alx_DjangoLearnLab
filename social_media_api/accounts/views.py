from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from .serializers import (
    RegisterSerializer, LoginSerializer, UserPublicSerializer, ProfileUpdateSerializer
)

from .models import User

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"user": UserPublicSerializer(user).data, "token": token.key}, status=status.HTTP_201_CREATED,
                            content_type="application/json",
                            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"user": UserPublicSerializer(user).data, "token": token.key},
                            status=status.HTTP_200_OK,
                            content_type="application/json",
                            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        return Response(UserPublicSerializer(request.user).data)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)