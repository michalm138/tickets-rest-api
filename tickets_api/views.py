from django.shortcuts import render
from django.http import HttpResponse
from tickets_api import models
from tickets_api import static_tables
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

