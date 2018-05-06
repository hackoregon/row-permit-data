from django.test import TestCase
from rest_framework.test import APIClient


class RowPermitDataTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_200_response(self):
        response = self.client.get('/api/crashes/')
        assert response.status_code == 200
