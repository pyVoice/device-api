import json
from random import randint
from uuid import uuid4

from .test_setup import TestSetUp


class TestViews(TestSetUp):
    """
    Set of tests to test the API view funcionality
    """

    def test_cannot_register_device_without_data(self):
        """ Test if a Device cannot be registered without providing any data """

        # make the API request
        response = self.client.post(self.api_url)

        # expecting 400 - Bad Request
        self.assertEqual(response.status_code, 400)

    def test_can_register_device(self):
        """ Test if a Device can be registered using a API key and data """

        self.device_data = {
            "device_id": str(uuid4()),
            "operating_system": "Test OS",
            "location": "Django",
            "version": str(randint(0, 5)),
        }

        self.device_data = json.dumps(self.device_data)

        # make the API request
        self.response = self.client.post(
            self.api_url, self.device_data, content_type="application/json"
        )

        # expecting 201 - Resource Created
        self.assertEqual(self.response.status_code, 201)
