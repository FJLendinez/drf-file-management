from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from drf_file_management.models import File
from drf_file_management.serializers import FileSerializer


class FileAPIView(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    """
    post:
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return FileDownloadSerializer
    #     return self.serializer_class

    def perform_download(self, instance, user):
        pass

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_download(instance, request.user)
        return super(FileAPIView, self).retrieve(request, *args, **kwargs)
