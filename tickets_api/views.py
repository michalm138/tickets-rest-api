from tickets_api import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from tickets_api import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class CreateUser(CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UpdateUser(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetails(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        response_data = {}
        response_data['User'] = serializers.UserSerializer(
            models.User.objects.get(pk=request.user.pk)
        ).data
        return Response(response_data)
