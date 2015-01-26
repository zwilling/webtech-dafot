from django import forms
from django.conf import settings


class SiteForm(forms.Form):
    """
    Extended :class:`Form` object. Removes 'default :' after labels on the
    form.
    """
    def __init__(self, *args, **kwargs):
        # eliminate the colon (:) that is automatically added to form labels
        kwargs.setdefault('label_suffix', '')
        super(SiteForm, self).__init__(*args, **kwargs)


class CourseForm(SiteForm):
    """
    Extended :class:`SiteForm` with `name` and `description` fields.
    """
    name = forms.CharField(
        max_length=255, required=True, label=u'Course name'
    )
    description = forms.CharField(
        max_length=5000, required=True, label=u'Course description',
        widget=forms.Textarea()
    )

    def clean_name(self):
        """
        Return a copy of the field 'name' with leading and trailing
        whitespace removed.
        """
        value = self.cleaned_data.get('name', '')
        value = value.strip()
        return value


class AssignmentForm(SiteForm):
    """
    Extended :class:`SiteForm` with `name`,`description`, `language`,
    `template_code` and `verification_code` fields.
    """
    name = forms.CharField(
        max_length=255, required=True, label=u'Assignment name'
    )
    description = forms.CharField(
        max_length=5000, required=True, label=u'Assignment description',
        widget=forms.Textarea()
    )
    language = forms.ChoiceField(
        required=True, label=u'Language', choices=settings.LANGUAGES
    )
    template_code = forms.CharField(
        required=True, label=u'Template code', widget=forms.Textarea()
    )
    verification_code = forms.CharField(
        required=True, label=u'Verification code', widget=forms.Textarea()
    )


class SolutionForm(SiteForm):
    """
    Extended :class:`SiteForm` with `code` field.
    """
    code = forms.CharField(
        required=True, label=u'Code', widget=forms.Textarea()
    )
