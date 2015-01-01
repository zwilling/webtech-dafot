from registration.forms import RegistrationFormUniqueEmail
from django import forms


class AppUserForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField(label="First name", required=True)
    last_name = forms.CharField(label="Last name", required=True)

    def __init__(self, *args, **kwargs):
        super(AppUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': 'The {fieldname} field is required'.format(
                    fieldname=unicode(field.label)
                )}