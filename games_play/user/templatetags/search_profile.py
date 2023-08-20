from django import template
from ..models import User

register = template.Library()

@register.simple_tag
def found_user():
    return User.objects.first()
