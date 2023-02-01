import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

# Test scenario - two prices 

    def test_list_of_two_prices(self):
        prices = [8, 16]
        expected_discount = None 
        self.assertEqual(expected_discount, discount(prices))

# Test scenario - one price 

    def test_list_of_one_prices(self):
        prices =[20]
        expected_discount = None
        self.assertEqual(expected_discount, discount(prices))

# test scenario - Zero values 

    def test_prices_that_are_zero(self):
        prices = [0,0,0,]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

# test scenario - Equal prices - same value 

    def test_equal_prices(self):
        prices = [9,9,9]
        expected_discount = 9
        self.assertEqual(expected_discount, discount(prices))

# test scenario - Negative prices - values 

    def test_negative_numbers(self):
        prices = [10, 34, -45, -35, -98, -455]
        with self.assertRaises(ValueError):
            discount(prices)


if __name__ == '__main__':
    unittest.main()