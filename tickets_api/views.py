from tickets_api import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from tickets_api import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


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



