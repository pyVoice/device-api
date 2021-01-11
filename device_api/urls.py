from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework import routers

from api.views import DeviceViewSet


favicon_view = RedirectView.as_view(
    url='https://assets.pyvoice.tech/wordpress/cropped-android-chrome-512x512-1-32x32.png', permanent=True)

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    # API Endpoints
    path('', include(router.urls)),

    path('admin/', admin.site.urls),
    path('favicon.ico', favicon_view)
]

admin.site.site_header = 'pyVoice API'
admin.site.index_title = 'Devices API'
admin.site.site_title = 'pyVoice API'
