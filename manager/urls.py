from django.urls import path, include
from .views import reservation_list, applications_list

urlpatterns = [
    path('reservations', reservation_list),
    path('applications', applications_list)
]