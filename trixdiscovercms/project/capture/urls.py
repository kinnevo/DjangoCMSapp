from django.conf.urls import include, patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

import os

urlpatterns = patterns('',
#    url(r'^capture/$', 'demo', name="capture"),
    url(r'^capture/$', 'capture.views.demo'),
)
