from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve
from entries.views import HomePage


BOOTSTRAP_VERSION = 'bootstrap/4.4.1'


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, HomePage)

    def test_home_page_redirects_anonymous(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
