from django import template

register = template.Library()

@register.filter
def embebido_uris(value):
    return value.replace('https://www.youtube.com/watch?v=','https://www.youtube.com/embed/')