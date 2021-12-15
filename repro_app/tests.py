from django.test import TestCase

from repro_app.models import ReproExample


class TestReproModel(TestCase):
    def test_startswith_includes_underscore(self):
        # given
        ReproExample.objects.create(value="foo_bar1234")

        # when
        found = ReproExample.objects.filter(value__startswith="foo_bar")

        # then
        self.assertEqual(found.count(), 1)

    def test_startswith_includes_backslash(self):
        # given
        ReproExample.objects.create(value="foo\\bar1234")

        # when
        found = ReproExample.objects.filter(value__startswith="foo\\bar")

        # then
        self.assertEqual(found.count(), 1)

    def test_startswith_includes_percent(self):
        # given
        ReproExample.objects.create(value="foo%bar1234")

        # when
        found = ReproExample.objects.filter(value__startswith="foo%bar")

        # then
        self.assertEqual(found.count(), 1)