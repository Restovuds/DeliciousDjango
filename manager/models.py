from django.core.validators import RegexValidator
from django.db import models
from django.template.defaultfilters import default
from django.utils import timezone



class UserReservation(models.Model):
    mobile_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Wrong phone number')

    name = models.CharField(max_length=120)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=15, validators=[mobile_re])
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    number_of_people = models.SmallIntegerField(default=1)
    message = models.TextField(max_length=500, blank=False)

    is_processed = models.BooleanField(default=False)
    time_of_receipt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'New receipt from {self.name}, {self.phone} - {self.time_of_receipt}'

    class Meta:
        ordering = ('time_of_receipt',)