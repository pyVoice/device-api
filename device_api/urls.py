from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework import routers

from api.views import DeviceViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet, basename='device')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]

admin.site.site_header = 'pyVoice API'
admin.site.index_title = 'Devices API'
admin.site.site_title = 'pyVoice API'
