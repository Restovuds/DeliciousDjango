from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import UserReservation, UserContact


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager, login_url='/login/')
def reservation_list(request):
    reservations = UserReservation.objects.filter(is_processed=False)
    return render(request,
                  template_name='reservation_list.html',
                  context={
                      'reservations': reservations
                  })


@login_required(login_url='/login/')
@user_passes_test(is_manager, login_url='/login/')
def applications_list(request):
    applications = UserContact.objects.filter(is_processed=False)
    return render(request,
                  template_name='applications_list.html',
                  context={
                      'applications': applications
                  })

@login_required(login_url='/login/')
@user_passes_test(is_manager, login_url='/login/')
def reservation(request, reservation_id):
    reservation_item = UserReservation.objects.get(pk=reservation_id)
    return render(request, template_name='reservation.html',
                  context={
                      'reservation': reservation_item
                  })


@login_required(login_url='/login/')
@user_passes_test(is_manager, login_url='/login/')
def application(request, application_id):
    """
    :param request: request object
    :param application_id: int, id of the application
    :return: QuerySet of the application
    """
    application_item = UserContact.objects.get(pk=application_id)
    return render(request, template_name='application.html',
                  context={
                      'application': application_item
                  })

@login_required(login_url='/login/')
@user_passes_test(is_manager, login_url='/login/')
def reservation_update(request, reservation_id):
    UserReservation.objects.filter(pk=reservation_id).update(is_processed=True)
    return redirect('manager:reservations')

@login_required(login_url='/login/')
@user_passes_test(is_manager, login_url='/login/')
def application_update(request, application_id):
    UserContact.objects.filter(pk=application_id).update(is_processed=True)
    return redirect('manager:applications')