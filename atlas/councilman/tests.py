from django.test import TestCase
from django.shortcuts import resolve_url

# Create your tests here.

class TestGet(TestCase):

    def setUp(self):
        self.response = self.client.get(resolve_url('index'))

    def test_http_ok(self):
        self.assertEqual(200, self.response.status_code)
