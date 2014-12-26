from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Course(models.Model):
    name = models.CharField(max_length = 255, blank = False, null = False, verbose_name = u'Course name')
    description = models.TextField(max_length = 5000, verbose_name = u'Course description', blank = True, null = True)
    organizer = models.ForeignKey(User, verbose_name = u'Organizer', related_name = 'courses')

class Assignment(models.Model):
    name = models.CharField(max_length = 255, blank = False, null = False, verbose_name = u'Assignment name')
    description = models.TextField(max_length = 5000, verbose_name = u'Assignment description', blank = True, null = True)
    template_code = models.TextField(max_length = 5000, verbose_name = u'Template code', blank = True, null = True)
    verification_code = models.TextField(max_length = 5000, verbose_name = u'Verification code', blank = True, null = True)
    course = models.ForeignKey(Course, verbose_name = u'Course', related_name = 'assignments')

class Solution(models.Model):
    code = models.TextField(max_length = 5000, verbose_name = u'Code', blank = True, null = True)
    exceptions = models.TextField(max_length = 5000, verbose_name = u'Exception', blank = True, null = True)
    grade = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
    assignment = models.ForeignKey(Assignment, verbose_name = u'Assignment', related_name = 'solutions')

class Attendee(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    class Meta:
        unique_together = ("user","course")