from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'profession'
        )


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'profession', 'password', 'confirm_password', 'date_of_birth')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password before saving
        user = User.objects.create_user(**validated_data)
        return user

class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")
        
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password")
        
        refresh = RefreshToken.for_user(user)
        return {
            "user": UserProfileSerializer(user).data,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }
