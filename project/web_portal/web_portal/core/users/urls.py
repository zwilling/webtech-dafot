from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView

from .forms import AppUserForm
from .views import CustomRegistrationView

urlpatterns = patterns('',
    url(r'^accounts/register/$', CustomRegistrationView.as_view(
        form_class=AppUserForm), {'title': 'Registration'}, name='register'),
    url(r'^accounts/login/$', auth_views.login,
        {'template_name': 'registration/login.html'}, name='auth_login'),
    url(r'^accounts/logout/$', auth_views.logout,
        {'template_name': 'registration/logout.html'}, name='auth_logout'),
    url(r'^accounts/activate/complete/$', TemplateView.as_view(
        template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', ActivationView.as_view(),
        name='registration_activate'),
    url(r'^accounts/register/$', RegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/register/complete/$', TemplateView.as_view(
        template_name='registration/registration_complete.html'),
        name='registration_complete'),
)