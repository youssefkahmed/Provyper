from django.urls import path

from . import views

urlpatterns = [
    path('/', views.home, name='home'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('request_appointment/', views.request_appointment, name='request'),
]
