from django.conf.urls import patterns, include
from .forms import AppUserForm
from .views import CustomRegistrationView

urlpatterns = patterns('',
    (r'^accounts/register/$', CustomRegistrationView.as_view(
        form_class=AppUserForm), {'title': 'Registration'}),
    (r'^accounts/', include('registration.backends.default.urls')),
)