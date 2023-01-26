from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLs
        fields = ('id', 'address', 'threshold', 'user', 'created_at', 'updated_at', 'failed_times')
        read_only_fields = ('created_at', 'updated_at', 'user', 'id', 'failed_times')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('id', 'created_at', 'updated_at', 'url', 'result')
