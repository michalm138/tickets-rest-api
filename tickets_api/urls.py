from django.urls import path
from tickets_api import views

urlpatterns = [
    path('hello/', views.hello, name='hello')
]