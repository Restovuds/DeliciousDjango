from django.urls import path, include
from .views import (reservation_list, reservation, reservation_update,
                    applications_list, application, application_update)

app_name = 'manager'

urlpatterns = [
    path('reservations', reservation_list, name='reservations'),
    path('reservation/<int:reservation_id>', reservation, name='reservation'),
    path('reservation/update/<int:reservation_id>', reservation_update, name='reservation_close'),

    path('applications', applications_list, name='applications'),
    path('application/<int:application_id>', application, name='application'),
    path('application/update/<int:application_id>', application_update, name='application_close'),


]