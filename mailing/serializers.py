from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import (
    User, Hour, Phone, Mailing, Message
)


class HourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hour
        fields = [
            'hour'
        ]


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = [
            'phone'
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'phone', 'name', 'key_phone', 'key_hour'
        ]


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = [
            'date', 'description', 'user', 'timestamp'
        ]
        read_only_fields = [
            'date', 'timestamp'
        ]


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'date', 'status', 'mailing', 'user', 'timestamp'
        ]
        read_only_fields = [
            'date', 'timestamp', 'status'
        ]
