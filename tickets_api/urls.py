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
]