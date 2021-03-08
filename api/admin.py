from django.contrib import admin

from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    actions = ["download_csv"]

    readonly_fields = (
        "id",
        "device_id",
        "registered_at",
        "version",
        "location",
        "operating_system",
    )
    list_display = (
        "device_id",
        "version",
        "location",
        "registered_at",
    )
    list_filter = ("version", "location", "operating_system")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    from .utils import download_csv

    download_csv.short_description = "Download CSV file of selected items"
