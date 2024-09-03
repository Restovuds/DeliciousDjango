from django.urls import path, include
from .views import reservation_list, reservation, applications_list, application

app_name = 'manager'

urlpatterns = [
    path('reservations', reservation_list, name='reservations'),
    path('reservation/<int:reservation_id>', reservation, name='reservation'),
    path('applications', applications_list, name='applications'),
    path('application/<int:application_id>', application, name='application'),
]