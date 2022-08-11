from atexit import register
import imp
from django import template
register = template.Library()
from linkpreview import link_preview

#returns title of url
@register.filter
def linktitle(url):
    return link_preview(url).title

#returns description of url
@register.filter
def linkdescription(url):
    return link_preview(url).description