from unittest import TestCase

from codekatas.codekatas.anagrams.anagrams import anagrams


class AnagramsTest(TestCase):
    def test_groups_tww_anagrams(self):
        d = anagrams(['abc', 'bca'])
        self.assertIn('abc', d)
        self.assertEqual({'abc', 'bca'}, set(d.get('abc')))

    def test_two_groups(self):
        d = anagrams(['ab', 'ba', 'cc'])
        self.assertEqual(
            {'ab': {'ab', 'ba'},
             'cc': {'cc', }}
            , d
        )
