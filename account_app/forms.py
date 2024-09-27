from .models import User
from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    pass1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    pass2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get('email')
        pass1 = cleaned_data.get("pass1")
        pass2 = cleaned_data.get("pass2")

        if pass1 and pass2 and pass1 != pass2:
            self.add_error("pass1", "Your passwords aren`t matched!")

        if User.objects.filter(username=username).exists() is True:
            self.add_error("username", "This Username exists!")

        if User.objects.filter(email=email).exists() is True:
            self.add_error("email", "This email exists!")

        User.objects.create_user(username=username, email=email, password=pass1)
