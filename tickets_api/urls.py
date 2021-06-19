from django.urls import path
from tickets_api import views

urlpatterns = [
    path('create/user/', views.CreateUser.as_view(), name='create-user')
]