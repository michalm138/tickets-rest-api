from tickets_api import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from tickets_api import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as drf_filters
import django_filters


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


class CreateCompany(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = models.Company.objects.all()
    serializer_class = serializers.CreateUpdateCompanySerializer


class UpdateCompany(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.CreateUpdateCompanySerializer

    def get_queryset(self):
        return models.Company.objects.filter(user=self.request.user)


class DeleteCompany(DestroyAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return models.Company.objects.filter(user=self.request.user)


class ListCompanies(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.CompanySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'name',
    ]
    ordering_fields = [
        'id',
        'name',
    ]

    def get_queryset(self):
        return models.Company.objects.filter(user=self.request.user)


class CreateEvent(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = models.Event.objects.all()
    serializer_class = serializers.CreateUpdateEventSerializer


class UpdateEvent(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.CreateUpdateEventSerializer

    def get_queryset(self):
        return models.Event.objects.filter(user=self.request.user)


class DeleteEvent(DestroyAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return models.Event.objects.filter(user=self.request.user)


class ListUserEvents(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'name',
    ]

    def get_queryset(self):
        return models.Event.objects.filter(user=self.request.user)


class ListEventsFiltering(django_filters.FilterSet):

    class Meta:
        model = models.Event
        fields = {
            'starts_at': ['gte'],
            'age_restrictions': ['gte'],
            'ticket_price': ['gte', 'lte']
        }


class ListEvents(ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = [
        'name',
        'city',
        'country__name',
        'company__name',
        'address',
        'user__first_name',
        'user__last_name',
        'user__username'
    ]
    filterset_class = ListEventsFiltering
