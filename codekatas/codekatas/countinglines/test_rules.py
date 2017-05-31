from unittest import TestCase

from codekatas.countinglines.rules import RegexRule
from codekatas.countinglines.states import Patterns


class TestRules(TestCase):
    def test_blank(self):
        rule = RegexRule(Patterns.blank)
        self.assertTrue(rule.applies('   ili'))
        self.assertFalse(rule.applies('ili   ili'))
        self.assertEqual('ili', rule.apply('   ili'))
        self.assertEqual('\n', rule.apply('   \n'))

    def test_comment_block(self):
        rule = RegexRule(Patterns.cb_enter)
        self.assertTrue(rule.applies('/*   ili'))
        self.assertFalse(rule.applies(' /*   ili'))
        self.assertEqual('ili', rule.apply('/*ili'))
        self.assertEqual('\n', rule.apply('/*\n'))

    def test_new_line(self):
        rule = RegexRule(Patterns.new_line)
        self.assertTrue(rule.applies('\n bla foo bar'))
        self.assertFalse(rule.applies(' \n'))
        self.assertEqual('ili', rule.apply('\nili'))
        self.assertEqual('', rule.apply('\n'))
