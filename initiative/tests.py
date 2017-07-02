from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from initiative.views import index, characters, monsters
from initiative.models import Character


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
        self.assertIn('<p> No characters are ready for battle.</p>', html)
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
        self.assertIn('<table>', html)
        self.assertTrue(html.endswith('</html>'))


class MonstersTest(TestCase):

    def test_root_url_resolves_to_monster_view(self):
        found = resolve('/monsters/')
        self.assertEqual(found.func, monsters)

    def test_monsters_returns_correct_html(self):
        request = HttpRequest()
        response = monsters(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n\n<html>'))
        self.assertIn('<title>Combat Tracker</title>', html)
        self.assertIn('<table>', html)
        self.assertTrue(html.endswith('</html>'))

class CharacterDetailTest(TestCase):

    def setUp(self):
        Character.objects.create(
            name = 'Aldo',
            initiative = 5,
            armor_class = 15,
            fortitude = 4,
            reflex = 6,
            will = 3,
            hit_points = 14
        )

    def still_concious_test(self):
        aldo = Character.objects.get(name='Aldo')
        self.assertTrue(aldo.still_conscious())
        aldo.damage_taken = 20
        slef.assertFalse(aldo.still_conscious())