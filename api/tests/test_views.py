from .test_setup import TestSetUp


class TestViews(TestSetUp):
    """
    Set of tests to test the API view funcionality
    """

    def test_cannot_register_device_without_data(self):
        """ Test if a Device cannot be registered without providing any data """
        # configure Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Api-Key ' + self.key)

        response = self.client.post(self.api_url)

        # 400 - Bad Request
        self.assertEqual(response.status_code, 400)

    def test_cannot_register_device_withou_api_key(self):
        """ Test if a Device cannot be registered without providing a API key """
        response = self.client.post(self.api_url)

        # 403 - Forbidden
        self.assertEqual(response.status_code, 403)
