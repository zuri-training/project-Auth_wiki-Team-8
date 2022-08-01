from .models import User
from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=150)
    lastname = serializers.CharField(max_length=150)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=80)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'username', 'password']


    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        email_exists = User.objects.filter(email=attrs['email']).exists()
        password_length = len(attrs['password'])

        if username_exists:
            raise serializers.ValidationError(detail="Username already exists")

        if email_exists:
            raise serializers.ValidationError(detail="Email already exists")

        if password_length < 8:
            raise serializers.ValidationError(detail="Password must be at least 8 characters long")

        return super().validate(attrs)