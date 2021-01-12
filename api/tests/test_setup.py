from uuid import uuid4
from random import randint
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_api_key.models import APIKey


class TestSetUp(APITestCase):
    def setUp(self) -> None:
        # the API url to query
        self.api_url = reverse('device-list')

        # API key to use in testing
        self.api_key, self.key = APIKey.objects.create_key(name='test-key')

        # data to create new Device
        # self.device_data = {
        #     'device_id': str(uuid4()),
        #     'operating_system': 'Test OS',
        #     'location': 'Django',
        #     'version': str(randint(0, 5))
        # }

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
