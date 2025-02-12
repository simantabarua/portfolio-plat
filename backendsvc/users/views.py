from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer, LogInSerializer
from rest_framework import generics, views
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class LogInAPIView(generics.GenericAPIView):
    serializer_class = LogInSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
