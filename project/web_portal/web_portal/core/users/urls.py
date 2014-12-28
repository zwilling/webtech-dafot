from django.conf.urls import patterns, url, include
from registration.backends.default.views import RegistrationView
from forms import AppUserForm
import views

urlpatterns = patterns('',
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=AppUserForm)),
    (r'^accounts/', include('registration.urls')),
)