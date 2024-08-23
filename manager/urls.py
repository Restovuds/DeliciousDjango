from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),


    #  reservation
    path('reservations/', reservations),
    path('reservation/<int:reservation_id>/', reservation),


    #  menu
    path('menu/', menu_items),
    path('menu/<int:item_id>/', menu_item),
    path('menu/add/', add_menu_item),
    path('menu/edit/<int:item_id>/', edit_menu_item),
    path('menu/delete/<int:item_id>/', delete_menu_item),


    # events
    path('events/', events_list),
    path('event/<int:event_id>/', view_event),
    path('event/add/', add_event),
    path('event/edit/<int:event_id>/', edit_event),
    path('event/delete/<int:event_id>/', delete_event),
]