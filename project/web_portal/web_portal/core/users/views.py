from forms import AppUserForm
from registration.signals import user_registered

def user_created(sender, user, request, **kwargs):
    """
    Called via signals when user registers. Creates different profiles and
    associations
    """
    form = AppUserForm(request.POST)
    # Update first and last name for user
    user.first_name = form.data['first_name']
    user.last_name = form.data['last_name']
    user.save()

#register for signals from django-registration to call your function after any registration is processed:
user_registered.connect(user_created)