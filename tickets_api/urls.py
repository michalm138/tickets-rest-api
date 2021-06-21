from django.urls import path
from tickets_api import views

urlpatterns = [
    path('user/create/', views.CreateUser.as_view(), name='create-user'),
    path('user/update/<int:pk>/', views.UpdateUser.as_view(), name='update-user'),
    path('user/details/', views.UserDetails.as_view(), name='user-details'),
]