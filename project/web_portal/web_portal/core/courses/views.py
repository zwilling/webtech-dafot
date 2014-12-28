from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from models import Course, Assignment, Solution, Attendee
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from forms import CourseForm, CourseSearchForm
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404, render

class CourseList(ListView, FormMixin):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = "courses"
    form_class = CourseSearchForm
    paginate_by = 2

    def dispatch(self, *args, **kwargs):
        return super(CourseList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_queryset(self):
        if self.form.is_valid():
            return Course.objects.filter(name__icontains=self.form.cleaned_data['name'])
        return Course.objects.all()

class AddCourse(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/add_course.html'

    @method_decorator(login_required(login_url = '/accounts/login/'))
    def dispatch(self, *args, **kwargs):
        return super(AddCourse, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AddCourse, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['edit'] = False
        return context

    def get_success_url(self):
        return reverse("course_list")

    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.organizer = self.request.user
        obj.save()
        return CreateView.form_valid(self, form)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_page.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated() and user.is_active and self.object.organizer == user:
            context['organizer'] = user
        else:
            context['organizer'] = None
        return context

def edit_course(request, id):
    pass

def delete_course(request, id):
    pass

course_list = CourseList.as_view()
add_course = AddCourse.as_view()
course_page = CourseDetailView.as_view()
