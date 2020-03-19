# django unnit test framework uses anything that starts with test a a test case
"""import django unnit test"""
from django.test import TestCase
"""import the function from which we are going to do the test"""
from app.calc import add subtract

class CalcTest(TestCase):

    # function to perform the test operation
    def test_add_numbers(self):
        """Test to make sure two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    # we are going to subtract two numbers using TDD
    def test_subtract_numbers(self):
        """test that certain values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)