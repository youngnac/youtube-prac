import urllib

from django import template

__all__ = (
    'get_encoded_dict'
)

register = template.Library()


@register.simple_tag
def get_encoded_dict(data_dict):
    return urllib.urlencode(data_dict)
