from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('patients/', views.patients, name='patients'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('appointments/', views.appointments, name='appointments'),
    path('add-appointment/', views.add_appointment, name='add_appointment'),
    path('add-doctor/', views.add_doctor),
]