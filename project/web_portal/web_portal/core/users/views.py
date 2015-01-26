import os

from registration.signals import user_registered
from registration.backends.default.views import RegistrationView

from .forms import AppUserForm
from .models import UserProfile


class CustomRegistrationView(RegistrationView):
    """Extended :class:`django.registration.RegistrationView` object with
    `title`."""

    def get_context_data(self, **kwargs):
        """Pass 'title' parameter to the template

        :param \*\*kwargs: Optional arguments that ``CustomRegistrationView`` takes.
        :returns: context kwargs
        """
        context = super(CustomRegistrationView, self).get_context_data(**kwargs)
        if 'title' in self.kwargs:
            context.update({'title': self.kwargs.get('title')})
        return context


def _user_created(sender, user, request, **kwargs):
    """
    Called via signals when user registers. Creates different profiles and
    associations

    :returns: None
    """
    form = AppUserForm(request.POST, request.FILES)
    # Update first and last name for user
    user.first_name = form.data['first_name']
    user.last_name = form.data['last_name']
    user.save()
    if request.FILES:
        avatar = request.FILES['avatar']
        name, ext = os.path.splitext(avatar.name)
        avatar.name = '{0}{1}'.format(user.id, ext)
        UserProfile.objects.create(user=user, avatar=avatar)
    else:
        UserProfile.objects.create(user=user)

# register for signals from django-registration to call function after
# any registration is processed:
user_registered.connect(_user_created)


