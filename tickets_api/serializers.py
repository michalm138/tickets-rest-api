from rest_framework import serializers
from tickets_api import models

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        ]