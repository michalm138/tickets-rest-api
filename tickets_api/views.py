from django.shortcuts import render
from django.http import HttpResponse
from tickets_api import models
from tickets_api import static_tables
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class FillStaticTables(APIView):

    def get(self, request):
        try:
            models.Country.objects.bulk_create(
                [models.Country(pk=record[0], name=record[1]) for record in static_tables.tables['Country']]
            )
            return Response('201 CREATED', status=status.HTTP_201_CREATED)
        except:
            return Response({'500 INTERNAL SERVER ERROR'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
