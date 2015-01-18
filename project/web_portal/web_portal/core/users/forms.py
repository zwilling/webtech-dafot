from registration.forms import RegistrationFormUniqueEmail
from django import forms

from .models import UserProfile


class AppUserForm(forms.ModelForm, RegistrationFormUniqueEmail):
    """Extended user registration form"""
    first_name = forms.CharField(label="First name", required=True)
    last_name = forms.CharField(label="Last name", required=True)

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email', 'password1',
                  'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        super(AppUserForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'widget': forms.FileInput})
        self.fields['avatar'].required = False
        for field, value in self.fields.iteritems():
            value.error_messages = {
                'required': 'The {fieldname} field is required'.format(
                    fieldname=unicode(value.label)
                )}
            if field == 'avatar':
                value.error_messages.update(
                    {'invalid_image': 'Invalid file format. Please upload an image.'})
