from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=2, max_length=255)
    last_name = serializers.CharField(min_length=2, max_length=255)
    email = serializers.EmailField(min_length=8, max_length=255)
    username = serializers.CharField(min_length=2, max_length=255)
    password = serializers.CharField(min_length=6, max_length=65, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
    

    def validate(self, attrs):
        # email = attrs.get('email', '')
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'Error': 'Email already in use'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)