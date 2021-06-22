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


class CreateUpdateCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = '__all__'

    def validate_user(self, data):
        if self.context['request'].user.pk != data.pk:
            raise serializers.ValidationError('You cannot assign company to other users.')
        return data


class CompanySerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(source='country.name')

    class Meta:
        model = models.Company
        fields = '__all__'


class CreateUpdateEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = '__all__'

    def validate(self, data):
        if data['starts_at'] > data['ends_at']:
            raise serializers.ValidationError({'Start_at': 'The start time has to be earlier than the end time.'})
        return data

    def validate_user(self, data):
        if self.context['request'].user.pk != data.pk:
            raise serializers.ValidationError('You cannot assign event to other users.')
        return data

    def validate_company(self, data):
        if data:
            if self.context['request'].user.pk != data.user.pk:
                raise serializers.ValidationError('You cannot assign company which belong to other user.')
        return data


class EventSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.username')
    company = serializers.StringRelatedField(source='company.name')
    country = serializers.StringRelatedField(source='country.name')

    class Meta:
        model = models.Event
        fields = '__all__'


class CreateTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ticket
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = models.Ticket
        fields = '__all__'