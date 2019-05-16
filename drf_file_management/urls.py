from django.urls import path, include
from rest_framework import routers

from drf_file_management.views import FileAPIView

router = routers.SimpleRouter()

router.register(r'file', FileAPIView)

app_name = 'drf_file_management'
urlpatterns = router.urls
