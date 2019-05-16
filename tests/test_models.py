#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_drf-file-management
------------

Tests for `drf-file-management` models module.
"""
import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files import File as CoreFile
from rest_framework import status
from rest_framework.test import APITestCase

from drf_file_management.models import File


class TestDrfFileManagement(APITestCase):

    def setUp(self):
        self.file_data = {'file': CoreFile(open('./tests/settings.py'), 'test_file.py')}
        self.file = File.objects.create(file=CoreFile(open("./tests/settings.py"),
                                                          "test_file_2.py"))
        self.user, _ = get_user_model().objects.get_or_create(username='test', password='test')

    def test_upload_file(self):
        self.client.force_authenticate(self.user)
        response = self.client.post('/file/', data=self.file_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_upload_file_if_user_is_not_logged_in(self):
        response = self.client.post('/file/', data=self.file_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_download_file(self):
        response = self.client.get('/file/{}/'.format(self.file.uuid))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_representation(self):
        self.assertTrue(str(self.file.uuid) in str(self.file))

    def tearDown(self):
        for path  in os.listdir(settings.MEDIA_ROOT or '.'):
            file_path = os.path.join(settings.MEDIA_ROOT, path)
            if os.path.isfile(file_path) and path.startswith('test_file'):
                os.remove(file_path)
