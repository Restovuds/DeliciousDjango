from django import forms
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class RegistrationUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput())

    def clean_repeat_password(self):
        data = self.cleaned_data
        if data['password'] == data['repeat_password']:
            return data['repeat_password']

        return forms.ValidationError('Passwords must match')


    class Meta:
        model = User
        fields = ('username',)



class LoginUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data['username'].strip()
        password = self.cleaned_data['password'].strip()

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                return forms.ValidationError('Incorrect username or password')
        return super().clean()



    class Meta:
        model = User
        fields = ('username', 'password')
