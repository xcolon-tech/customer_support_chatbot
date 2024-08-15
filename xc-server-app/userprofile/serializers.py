from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # or 'User' if using the default model
        fields = ['username', 'mobile', 'mpin', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            mobile=validated_data['mobile'],
            mpin=validated_data['mpin'],
            password=validated_data['password'],
        )
        return user

class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(required=True)
    mpin = serializers.CharField(required=True)

    def validate(self, data):
        user = authenticate(mobile=data['mobile'], mpin=data['mpin'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")