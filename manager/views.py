from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserReservation, UserContact


@login_required(login_url='/login/')
def reservation_list(request):
    reservations = UserReservation.objects.filter(is_processed=False)
    return render(request,
                  template_name='reservation_list.html',
                  context={
                      'reservations': reservations
                  })


@login_required(login_url='/login/')
def applications_list(request):
    applications = UserContact.objects.filter(is_processed=False)
    return render(request,
                  template_name='applications_list.html',
                  context={
                      'applications': applications
                  })
