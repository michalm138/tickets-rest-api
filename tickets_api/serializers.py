from rest_framework import serializers
from tickets_api import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            'pk',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        ]
        read_only_fields = ['pk']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if not data['first_name']:
            raise serializers.ValidationError('First name field is required.')
        if not data['last_name']:
            raise serializers.ValidationError('Last name field is required.')
        if self.context['view'].kwargs:
            if self.context['request'].user.pk != self.context['view'].kwargs['pk']:
                raise serializers.ValidationError('You cannot modify other users.')
        return data

    def create(self, validated_data):
        user = models.User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
