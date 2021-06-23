from django.urls import path
from tickets_api import views
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="API Documentation",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('user/create/', views.CreateUser.as_view(), name='create-user'),
    path('user/update/<int:pk>/', views.UpdateUser.as_view(), name='update-user'),
    path('user/details/', views.UserDetails.as_view(), name='user-details'),
    path('company/create/', views.CreateCompany.as_view(), name='create-company'),
    path('company/update/<int:pk>/', views.UpdateCompany.as_view(), name='update-company'),
    path('company/delete/<int:pk>/', views.DeleteCompany.as_view(), name='delete-company'),
    path('company/list/', views.ListCompanies.as_view(), name='list-companies'),
    path('event/create/', views.CreateEvent.as_view(), name='create-event'),
    path('event/update/<int:pk>/', views.UpdateEvent.as_view(), name='update-event'),
    path('event/delete/<int:pk>/', views.DeleteEvent.as_view(), name='delete-event'),
    path('event/list/', views.ListUserEvents.as_view(), name='user-list-event'),
    path('event/list/all/', views.ListEvents.as_view(), name='list-event'),
    path('event/stats/<int:pk>/', views.GetEventStats.as_view(), name='get-event-stats'),
    path('ticket/create/', views.CreateTicket.as_view(), name='create-ticket'),
    path('ticket/details/<uuid:id>/', views.TicketDetails.as_view(), name='ticket-details'),
    path('ticket/confirm/<uuid:pk>/', views.ConfirmTicket.as_view(), name='confirm-ticket'),
    # Swagger urls
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]