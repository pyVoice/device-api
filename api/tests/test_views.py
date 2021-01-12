from uuid import uuid4
from random import randint

from .test_setup import TestSetUp


class TestViews(TestSetUp):
    """
    Set of tests to test the API view funcionality
    """

    def test_cannot_register_device_without_data(self):
        """ Test if a Device cannot be registered without providing any data """

        # configure Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Api-Key ' + self.key)

        # make the API request
        response = self.client.post(self.api_url)

        # expecting 400 - Bad Request
        self.assertEqual(response.status_code, 400)

    def test_cannot_register_device_withou_api_key(self):
        """ Test if a Device cannot be registered without providing a API key """

        self.device_data = {
            'device_id': str(uuid4()),
            'operating_system': 'Test OS',
            'location': 'Django',
            'version': str(randint(0, 5))
        }

        # send the empty Authorization header
        self.client.credentials()

        # make the API request
        response = self.client.post(self.api_url)

        # expecting 403 - Forbidden
        self.assertEqual(response.status_code, 403)

    def test_can_register_device(self):
        """ Test if a Device can be registered using a API key and data """

        self.device_data = {
            'device_id': str(uuid4()),
            'operating_system': 'Test OS',
            'location': 'Django',
            'version': str(randint(0, 5))
        }

        # configure Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Api-Key ' + self.key)

        # make the API request
        self.response = self.client.post(
            self.api_url, self.device_data, content_type='application/json')

        # expecting 201 - Resource Created
        self.assertEqual(self.response.status_code, 201)

        # # expecting the added device data back
        # device_response = self.client.get(
        #     self.api_url + str(response.json()['id']))

        # self.assertEqual(device_response.json(), self.device_data)
