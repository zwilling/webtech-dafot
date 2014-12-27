from registration.forms import RegistrationFormUniqueEmail
from django import forms


class AppUserForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField(label="First_name")
    last_name = forms.CharField(label="Last_name")


