from django import forms
from manager.models import UserReservation

class UserReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, min_length=2, widget=forms.TextInput(attrs={
        'type':  "text",
        'name':  "name",
        'class': "form-control",
        'id': "name",
        'placeholder': "Your Name",
        'data-msg': "Please enter at least 2 chars",
    }))
    email = forms.EmailField(max_length=36, widget=forms.TextInput(attrs={
        'type': "email",
        'class': "form-control",
        'name': "email",
        'id': "email",
        'placeholder': "Your Email",
        'data-msg': "Please enter a valid email",
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'name': "phone",
        'id': "phone",
        'placeholder': "Your Phone",
        'data-msg': "Please enter at least 4 chars",
    }))
    date = forms.DateField(widget=forms.TextInput(attrs={
        'type': "text",
        'name': "date",
        'class': "form-control",
        'id': "date",
        'placeholder': "Date",
        'data-msg': "Please enter at least 4 chars",
    }))
    time = forms.TimeField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'name': "time",
        'id': "time",
        'placeholder': "Time",
        'data-msg': "Please enter at least 4 chars",
    }))
    number_of_people = forms.IntegerField(widget=forms.TextInput(attrs={
        'type': "number",
        'class': "form-control",
        'name': "people",
        'id': "people",
        'min': 1,
        'max': 10,
        'placeholder': "# of people",
        'data-msg': "Please enter at least 1 chars",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control",
        'name': "message",
        'rows': "5",
        'placeholder': "Message",
    }))

    class Meta:
        model = UserReservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'number_of_people', 'message',)
