from rest_framework import serializers
from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['device_id', 'version', 'operating_system',
                  'location', 'registered_at']

    # def validate_device_id(self, value):
    #     if not Device.objects.get(device_id=value).exists():
    #     	return value
    #     else:
    # 	    raise serializers.ValidationError('Device with that ID already exists.')
