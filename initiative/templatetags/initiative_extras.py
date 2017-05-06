from django import template

register = template.Library()


@register.filter
def sign(value):
    if value > 0:
        return f'+{value}'
    else:
        return f'{value}'