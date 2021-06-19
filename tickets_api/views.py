from django.shortcuts import render
from django.http import HttpResponse
from tickets_api import models
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from tickets_api import serializers


class CreateUser(CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.CreateUserSerializer