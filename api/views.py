from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, BasePermission

from api.models import Device

from .serializers import DeviceSerializer

SAFE_METHODS = ["POST", "PUT", "HEAD", "OPTIONS"]


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission class
    Only allow POST for anonymous requests, deny GET
    """

    def has_permission(self, request, view):
        if (
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
        ):
            return True
        return False


class DeviceViewSet(ModelViewSet):
    """
    API endpoints for Deviced related operations
    """

    queryset = Device.objects.all().order_by("-registered_at")
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
