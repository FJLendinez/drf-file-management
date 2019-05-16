# -*- coding: utf-8 -*-
from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('drf_file_management.urls', namespace='drf_file_management')),
]
