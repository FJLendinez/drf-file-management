from importlib import import_module

from django.conf import settings

from drf_file_management.models import File


def import_callable(path_or_callable):
    if hasattr(path_or_callable, '__call__'):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, str)
        package, attr = path_or_callable.rsplit('.', 1)
        return getattr(import_module(package), attr)


file_settings: dict = getattr(settings, 'FILE_MANAGEMENT', {})


class Config:
    FileModel = import_callable(file_settings.get('FILE_MODEL', File))
    FileUploadSerializer = import_callable(
        file_settings.get('FILE_UPLOAD_SERIALIZER', 'drf_file_management.serializers.FileSerializer'))
    FileDownloadSerializer = import_callable(
        file_settings.get('FILE_DOWNLOAD_SERIALIZER', 'drf_file_management.serializers.FileSerializer'))
