from django.urls import path
from tickets_api import views

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
    path('event/list/user/', views.ListUserEvents.as_view(), name='user-list-event'),
    path('event/list/', views.ListEvents.as_view(), name='list-event'),
    path('ticket/create/', views.CreateTicket.as_view(), name='create-ticket'),
    path('ticket/details/<uuid:id>/', views.TicketDetails.as_view(), name='ticket-details'),
    path('ticket/confirm/<uuid:pk>/', views.ConfirmTicket.as_view(), name='confirm-ticket'),
]