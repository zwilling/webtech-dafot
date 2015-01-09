from django import forms

LANGUAGES = (
    ('python', u'Python'),
    ('java', u'Java'),
    )


class SiteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        #eliminate the colon (:) that is automatically added to form labels
        kwargs.setdefault('label_suffix', '')
        super(SiteForm, self).__init__(*args, **kwargs)


class CourseForm(SiteForm):
    name = forms.CharField(max_length=255, required=True, label=u'Course name')
    description = forms.CharField(max_length=5000, required=True,
                                  widget=forms.Textarea(
                                      attrs={'cols': 60, 'rows': 10}),
                                  label=u'Course description')

    def clean_name(self):
        value = self.cleaned_data.get('name', '')
        value = value.strip()
        return value


class CourseSearchForm(SiteForm):
    name = forms.CharField(label=u'Course name', required=False)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CourseSearchForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        value = self.cleaned_data.get('name', '')
        value = value.strip()
        return value


class AssignmentForm(SiteForm):
    name = forms.CharField(max_length=255, required=True,
                           label=u'Assignment name')
    description = forms.CharField(max_length=5000, required=True,
                                  widget=forms.Textarea(
                                      attrs={'cols': 60, 'rows': 10}),
                                  label=u'Assignment description')
    template_code = forms.CharField(required=True, label=u'Template code',
                                    widget=forms.Textarea(
                                        attrs={'cols': 60, 'rows': 10}))
    verification_code = forms.CharField(required=True,
                                        widget=forms.Textarea(
                                            attrs={'cols': 60, 'rows': 10}),
                                        label=u'Verification code')
    language = forms.ChoiceField(required=True, label=u'Language',
                                 choices=[[r[0], r[1]] for r in LANGUAGES])


class SolutionForm(SiteForm):
    code = forms.CharField(required=True, label=u'Code',
                           widget=forms.Textarea(
                               attrs={'cols': 60, 'rows': 10}))
