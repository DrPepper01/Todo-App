from django import template
import datetime

register = template.Library()


@register.filter
def uppercase(value: str):
    return value.upper()

@register.simple_tag
def current_year():
    return datetime.datetime.now()

