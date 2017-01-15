from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from jinja2 import Environment

#customized filter
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters['datetime'] = datetimeformat
    return env
