from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Course(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False,
                            verbose_name=u'Course name')
    description = models.TextField(max_length=5000, blank=True, null=True,
                                   verbose_name=u'Course description')
    organizer = models.ForeignKey(User, verbose_name=u'Organizer',
                                  related_name='courses')


class Assignment(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False,
                            verbose_name=u'Assignment name')
    description = models.TextField(max_length=5000, blank=True, null=True,
                                   verbose_name=u'Assignment description')
    template_code = models.TextField(max_length=5000, blank=True, null=True,
                                     verbose_name=u'Template code')
    verification_code = models.TextField(max_length=5000, blank=True, null=True,
                                         verbose_name=u'Verification code')
    course = models.ForeignKey(Course, verbose_name=u'Course',
                               related_name='assignments')


class Solution(models.Model):
    code = models.TextField(max_length=5000, blank=True, null=True,
                            verbose_name=u'Code')
    exceptions = models.TextField(max_length=5000, blank=True, null=True,
                                  verbose_name=u'Exception')
    grade = models.FloatField(validators=[MinValueValidator(0.0),
                                          MaxValueValidator(10.0)])
    assignment = models.ForeignKey(Assignment, verbose_name=u'Assignment',
                                   related_name='solutions')


class Attendee(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)

    class Meta:
        unique_together = ("user","course")