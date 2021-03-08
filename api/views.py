from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey

from api.models import Device

from .serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoints for Deviced related operations
    """

    queryset = Device.objects.all().order_by("-registered_at")
    serializer_class = DeviceSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
