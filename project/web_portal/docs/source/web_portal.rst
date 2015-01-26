.. _library-web-portal:

**********
Web Portal
**********

Introduction
============
`Web Portal` is a part of our project which interacts with the user, like a 
usual web-site. It is built with a Django Web Framework, Bootstrap Framework
and uses JavaScript, CodeMirror and prism.js library. It consists of several 
modules: main, users, courses, errors.

Deployment
==========
This part of the documentation covers the deployment of `Web Portal` on local 
system. The first step to using any software package is getting it properly 
installed.

Get the Code
------------
`Web Portal` is actively developed on GitHub, where the code is
`always available <https://github.com/azastupailo/Code-Project>`_.

You can either clone the public repository::

    $ git clone git://github.com/azastupailo/Code-Project.git

Pip & Virtualenv
----------------
``pip`` is a package management system used to install and manage software 
packages written in Python. 

Please install ``pip`` by following 
`this link <https://pip.pypa.io/en/latest/installing.html>`_.

.. warning::

   Please don't proceed to the next steps before installing ``pip``.


``virtualenv`` is a tool to create isolated Python environments. It creates 
an environment that has its own installation directories, that doesn't share 
libraries with other virtualenv environments (and optionally doesn't access 
the globally installed libraries either).
You can install ``python-virtualenv`` and use for a project or you can use 
your regular Python environment in the system. to install ``virtualenv``
please follow `this link <https://virtualenv.pypa.io/en/latest/installation.html>`_.

So, if you have installed ``virtualenv``, first you need to create and 
activate it::

    $ cd <code-project-dir>
    $ virtualenv venv
    $ source venv/bin/activate

To deactivate ``virtualenv`` later just simply type::

    $ deactivate

Now we can install all the dependecies for `Web Portal`. 

.. warning::

   `Web Portal` uses ``PostgreSQL`` database. Please make sure that it is installed in 
   your system.

Installing python packages is simple, just run this in your terminal::

    $ pip install -r requirements.txt

Please specify database connection parameters in the ``web_portal/settings.py`` file:: 

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'database-name',
            'USER': 'user-name',
            'PASSWORD': 'password',
            'HOST': 'host',
            'PORT': 'port',
        }
    }

And email parameters used for sending activation link to the users at `Web Portal`::

    DEFAULT_EMAIL = 'my.email@gmail.com'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'my.email'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_USE_TLS = True

Now let's synchronize the database now::

    $ python manage.py syncdb

And simply run the `Web Portal`::

    $ python manage.py runserver

Developer Interface
===================
This part of the documentation covers all the interfaces of `Web Portal`. 
For parts where `Web Portal` depends on external libraries, we document the most 
important right here and provide links to the canonical documentation.

As we have already mentioned, `Web Portal` consists of several modules:
main, users, courses and errors.

main module
-----------
This module is responsible for following views::

    http://your.domain.com/
    http://your.domain.com/index
    http://your.domain.com/coming
    http://your.domain.com/our-team

.. autofunction:: core.main.views.index
.. autofunction:: core.main.views.coming
.. autofunction:: core.main.views.our_team

users module
------------
This module is responsible for following views::

    http://your.domain.com/accounts/register/
    http://your.domain.com/accounts/register/complete/
    http://your.domain.com/accounts/login/
    http://your.domain.com/accounts/logout/
    http://your.domain.com/accounts/activate/<activation_key>/
    http://your.domain.com/accounts/activate/complete/

.. autoclass:: core.users.models.UserProfile
.. autoclass:: core.users.views.CustomRegistrationView
.. autoclass:: core.users.forms.AppUserForm

courses module
--------------
This module is responsible for following views::

    http://your.domain.com/courses/
    http://your.domain.com/courses/add/
    http://your.domain.com/courses/<course_id>/
    http://your.domain.com/courses/<course_id>/delete/
    http://your.domain.com/courses/<course_id>/attend/
    http://your.domain.com/courses/<course_id>/assignments/add/
    http://your.domain.com/courses/<course_id>/assignments/<assignment_id>/
    http://your.domain.com/courses/<course_id>/assignments/<assignment_id>/solutions/
    http://your.domain.com/courses/<course_id>/assignments/<assignment_id>/solutions/<solution_id>/    
    http://your.domain.com/courses/<course_id>/attendee/<attendee_id>/solutions/

api.py
++++++

.. autofunction:: core.courses.api.get_courses
.. autofunction:: core.courses.api.get_course
.. autofunction:: core.courses.api.get_assignments
.. autofunction:: core.courses.api.get_assignment
.. autofunction:: core.courses.api.get_solutions
.. autofunction:: core.courses.api.get_attendee_solutions
.. autofunction:: core.courses.api.get_user_avatar_url
.. autofunction:: core.courses.api.create_course
.. autofunction:: core.courses.api.create_assignment
.. autofunction:: core.courses.api.create_solution
.. autofunction:: core.courses.api.attend_course
.. autofunction:: core.courses.api.delete_course


forms.py
++++++++
.. autoclass:: core.courses.forms.SiteForm
.. autoclass:: core.courses.forms.CourseForm
.. autoclass:: core.courses.forms.AssignmentForm
.. autoclass:: core.courses.forms.SolutionForm

views.py
++++++++
.. autofunction:: core.courses.views.course_list
.. autofunction:: core.courses.views.course_page
.. autofunction:: core.courses.views.assignment_page
.. autofunction:: core.courses.views.solution_page
.. autofunction:: core.courses.views.add_course
.. autofunction:: core.courses.views.add_assignment
.. autofunction:: core.courses.views.add_solution
.. autofunction:: core.courses.views.attend_course
.. autofunction:: core.courses.views.attendee_solutions
.. autofunction:: core.courses.views.delete_course

utils.py
++++++++
.. autofunction:: core.courses.utils.base_request_url
.. autofunction:: core.courses.utils.json_object_hook
.. autofunction:: core.courses.utils.get_page_from_request
.. autofunction:: core.courses.utils.user_is_attendee
.. autofunction:: core.courses.utils.user_is_organizer
.. autofunction:: core.courses.utils.process_request
.. autofunction:: core.courses.utils.send_get_request
.. autofunction:: core.courses.utils.send_post_request
.. autofunction:: core.courses.utils.send_delete_request
.. autofunction:: core.courses.utils.prepare_headers

errors module
-------------
This module is responsible for following custome errors views.

views.py
++++++++
.. autofunction:: core.errors.views.bad_request
.. autofunction:: core.errors.views.permission_denied
.. autofunction:: core.errors.views.page_not_found
.. autofunction:: core.errors.views.server_error