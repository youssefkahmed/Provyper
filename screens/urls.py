from django.urls import path

from . import views

urlpatterns = [
    path('screens/', views.home, name='home'),
    path('screens/confirmation/', views.confirmation, name='confirmation'),
    path('screens/request_appointment/', views.request_appointment, name='request'),
]
