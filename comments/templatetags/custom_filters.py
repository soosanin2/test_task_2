from django import template

register = template.Library()

@register.filter
def has_txt_extension(value):
    return value.name.lower().endswith('.txt')