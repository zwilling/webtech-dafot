from django.template import Library

register = Library()

@register.inclusion_tag('layout_form.html')
def layout_form(form):
    return {'form' : form}