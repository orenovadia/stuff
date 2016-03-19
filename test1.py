import unittest
class TestClass1(unittest.TestCase):
    def test_meself(self):
        assert 1==1
    def test_bad(self):
        assert 1==2

