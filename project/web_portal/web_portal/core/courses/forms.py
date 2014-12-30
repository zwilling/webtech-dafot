from django import forms
from django.forms import Textarea

class CourseForm(forms.Form):
    name = forms.CharField(max_length=255, required=True,
                            label=u'Course name')
    description = forms.CharField(max_length=5000, required=True, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),
                                   label=u'Course description')

    def clean_name(self):
        value = self.cleaned_data.get('name', '')
        value = value.strip()
        return value

class CourseSearchForm(forms.Form):
    name = forms.CharField(label=u'Course name', required=False)

    def clean_name(self):
        value = self.cleaned_data.get('name', '')
        value = value.strip()
        return value

class AssignmentForm(forms.Form):
    name = forms.CharField(max_length=255, required=True,
                            label=u'Assignment name')
    description = forms.CharField(max_length=5000, required=True, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),
                                   label= u'Assignment description')
    template_code = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),
                                    label=u'Template code')
    verification_code = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),
                                    label=u'Verification code')