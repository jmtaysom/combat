from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from initiative.views import index, characters


class IndexTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n\n<html>'))
        self.assertIn('<title>Combat Tracker</title>', html)
        self.assertTrue(html.endswith('</html>'))


class CharactersTest(TestCase):

    def test_root_url_resolves_to_chaaracter_view(self):
        found = resolve('/characters/')
        self.assertEqual(found.func, characters)

    def test_characters_returns_correct_html(self):
        request = HttpRequest()
        response = characters(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n\n<html>'))
        self.assertIn('<title>Combat Tracker</title>', html)
        self.assertTrue(html.endswith('</html>'))