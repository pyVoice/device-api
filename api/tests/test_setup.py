from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    def setUp(self) -> None:
        # the API url to query
        self.api_url = reverse("device-list")

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
