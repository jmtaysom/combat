from django import template

register = template.Library()


@register.filter
def sign(value):
    if value > 0:
        return '+{}'.format(value)
    else:
        return '{}'.format(value)