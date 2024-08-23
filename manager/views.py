from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello, manager")

def reservations(request):
    return HttpResponse("<h1>Reservations list</h1>")


def reservation(request, reservation_id):
    return HttpResponse(f"<h1>Reservation with id{reservation_id}</h1>")


def menu_items(request):
    return HttpResponse("<h1>Menu list</h1>")


def menu_item(request, item_id):
    return HttpResponse(f"<h1>Item with id{item_id} in Menu</h1>")


def add_menu_item(request):
    return HttpResponse("<h1>Add Menu</h1>")


def edit_menu_item(request, item_id):
    return HttpResponse(f"<h1>Edit item with id{item_id} in Menu</h1>")


def delete_menu_item(request, item_id):
    return HttpResponse(f"<h1>Delete item with id{item_id} from Menu</h1>")


def events_list(request):
    return HttpResponse("<h1>Events list</h1>")


def view_event(request, event_id):
    return HttpResponse(f"<h1>Event with id{event_id}</h1>")


def add_event(request):
    return HttpResponse("<h1>Add Event</h1>")


def edit_event(request, event_id):
    return HttpResponse(f"<h1>Edit Event with id{event_id}</h1>")


def delete_event(request, event_id):
    return HttpResponse(f"<h1>Delete Event with id{event_id}</h1>")
