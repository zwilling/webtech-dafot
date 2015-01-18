from django import forms

LANGUAGES = (
    ('python', u'Python'),
    ('java', u'Java')
)


class SiteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # eliminate the colon (:) that is automatically added to form labels
        kwargs.setdefault('label_suffix', '')
        super(SiteForm, self).__init__(*args, **kwargs)


class CourseForm(SiteForm):
    name = forms.CharField(
        max_length=255, required=True, label=u'Course name'
    )
    description = forms.CharField(
        max_length=5000, required=True, label=u'Course description',
        widget=forms.Textarea()
    )

    def clean_name(self):
        value = self.cleaned_data.get('name', '')
        value = value.strip()
        return value


class AssignmentForm(SiteForm):
    name = forms.CharField(
        max_length=255, required=True, label=u'Assignment name'
    )
    description = forms.CharField(
        max_length=5000, required=True, label=u'Assignment description',
        widget=forms.Textarea()
    )
    language = forms.ChoiceField(
        required=True, label=u'Language', choices=LANGUAGES
    )
    template_code = forms.CharField(
        required=True, label=u'Template code', widget=forms.Textarea()
    )
    verification_code = forms.CharField(
        required=True, label=u'Verification code', widget=forms.Textarea()
    )


class SolutionForm(SiteForm):
    code = forms.CharField(
        required=True, label=u'Code', widget=forms.Textarea()
    )
