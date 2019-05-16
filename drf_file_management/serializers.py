from rest_framework import serializers

from drf_file_management.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'file',
            'uuid',
            'modified',
            'created'
        )
        read_only_fields = ('uuid', 'modified', 'created')
        model = File
