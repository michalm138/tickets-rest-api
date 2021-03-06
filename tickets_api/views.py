from tickets_api import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from tickets_api import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters


class CreateUser(CreateAPIView):
    permission_classes = ()
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
    permission_classes = ()
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


class CreateTicket(CreateAPIView):
    permission_classes = ()
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.CreateTicketSerializer


class TicketDetails(APIView):

    def get(self, request, *args, **kwargs):
        response_data = {}
        response_data['ticket'] = serializers.TicketSerializer(
            models.Ticket.objects.get(id=kwargs['id'])
        ).data
        return Response(response_data)


class ConfirmTicket(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.ConfirmTicketSerializer
    http_method_names = ['patch']

    def get_queryset(self):
        return models.Ticket.objects.filter(event__user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(confirmed=True)


class GetEventStats(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        response_data = {}
        event_instance = models.Event.objects.get(pk=kwargs['pk'])
        ticket_instance = models.Ticket.objects.filter(event=event_instance)
        if event_instance.user == request.user:
            response_data['event_details'] = serializers.EventSerializer(event_instance).data
            response_data['sold_tickets'] = serializers.TicketStatsSerializer(ticket_instance, many=True).data
            return Response(response_data)
        else:
            return Response({'error:': 'You do not have access to see stats of this event.'})
