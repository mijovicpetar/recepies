"""Calc test module."""
from django.test import TestCase
from app.calc import add, sub


class CalcTestCase(TestCase):
    """Calc unit test module."""
    def test_add(self):
        """Test add two numbers."""
        self.assertEqual(add(6, 5), 11)

    def test_sub(self):
        """Test substract two numbers."""
        self.assertEqual(sub(6, 5), 1)
