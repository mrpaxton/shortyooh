from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    # for everything else in the url other than www
    host(r'(?!www).*', 'shorturl.hostsconf.urls', name='wildcard'),
)
