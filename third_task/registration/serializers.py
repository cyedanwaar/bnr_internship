from rest_framework import serializers
from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'admin_or_staff']

    def validate(self, attrs):
        username = str(attrs.get('username', '')).strip()

        if not username.isalnum():
            raise serializers.ValidationError("Only alphanumeric characters are allowed for username! ")
        
        if len(username) < 4:
            raise serializers.ValidationError("Username must contain atleast 4 characters")
        
        return attrs
    
    def create(self, validated_data):
        admin_or_staff = validated_data.get('admin_or_staff')
        if not admin_or_staff:
            return User.objects.create_user(**validated_data)
        elif admin_or_staff == 'admin':
            return User.objects.create_admin(**validated_data)
        else:
            return User.objects.create_staff(**validated_data)

