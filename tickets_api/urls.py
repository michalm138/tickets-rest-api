from django.urls import path
from tickets_api import views

urlpatterns = [
    path('conf/fill_static_tables/', views.FillStaticTables.as_view(), name='hello')
]