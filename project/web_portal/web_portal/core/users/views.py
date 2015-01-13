from registration.signals import user_registered
from registration.backends.default.views import RegistrationView
from .forms import AppUserForm
from .models import UserProfile
import os


class CustomRegistrationView(RegistrationView):

    def get_context_data(self, **kwargs):
        context = super(CustomRegistrationView, self).get_context_data(**kwargs)
        if 'title' in self.kwargs:
            context.update({'title': self.kwargs.get('title')})
        return context


def user_created(sender, user, request, **kwargs):
    """
    Called via signals when user registers. Creates different profiles and
    associations
    """
    form = AppUserForm(request.POST, request.FILES)
    # Update first and last name for user
    user.first_name = form.data['first_name']
    user.last_name = form.data['last_name']
    user.save()
    print('here1')
    if request.FILES:
        avatar = request.FILES['avatar']
        name, ext = os.path.splitext(avatar.name)
        avatar.name = '{0}{1}'.format(user.id, ext)
        print('here2')
        UserProfile.objects.create(user=user, avatar=avatar)
        print('here3')
    else:
        UserProfile.objects.create(user=user)
# register for signals from django-registration to call your function after
# any registration is processed:
user_registered.connect(user_created)


