from django import template
from dko.models import *
register=template.Library()

@register.inclusion_tag('main/tags/show_sidebar.html')
def show_sidebar():
    side_bar = Client.objects.all()
    return {'side_bar':side_bar,}