from django import forms
from django.forms import Textarea
from models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('organizer',)
        widgets = {'text': Textarea(attrs={'cols': 60, 'rows': 10})}


class CourseSearchForm(forms.Form):
    name = forms.CharField(label='Course name', required=False)

    def clean_name(self):
        value = self.cleaned_data.get('name', '')
        value = value.strip()
        return value