import uuid
from django.db import models
from django.utils import timezone


class Device(models.Model):
    device_id = models.CharField(max_length=40, unique=True,
    	verbose_name='Device ID',
    	help_text='A unique ID to identify each device')
    version = models.CharField(max_length=10,
    	verbose_name='Version',
    	help_text='The pyVoice version installed')
    registered_at = models.DateTimeField(auto_now=True,
    	verbose_name='Registered at',
    	help_text='The date and time the device was registered')
    operating_system = models.CharField(max_length=50,
    	verbose_name='Operating System',
    	help_text='The operating system name, edition and architecture')
    location = models.CharField(max_length=100,
    	verbose_name='Location',
    	help_text='The location of the device (city/country)')

    @property
    def times(self):
        # fix for Grafana charts
        timestamp = str(self.registered_at.timestamp()).split('.', 1)[0]

        times_dict = {
            'full': self.registered_at,
            'timestamp': int(timestamp),
            'date': self.registered_at.strftime('%Y-%m-%d'),
            'time': self.registered_at.strftime('%H:%M:%S'),
        }

        return times_dict

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    def __str__(self):
    	return self.device_id