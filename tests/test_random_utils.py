import sys
import os
import unittest
from unittest.mock import patch

# Add the parent directory to sys.path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from init.random_utils import (
    generate_random_string,
    generate_random_number,
    generate_random_list,
    shuffle_list,
    random_choice,
    generate_random_float,
    generate_random_boolean
)

class TestRandomUtils(unittest.TestCase):

    def test_generate_random_string(self):
        # Test length
        s = generate_random_string(length=15)
        self.assertEqual(len(s), 15)
        
        # Test digits inclusion
        s_digits = generate_random_string(length=100, include_digits=True, include_special=False)
        self.assertTrue(any(c.isdigit() for c in s_digits))
        
        # Test special chars inclusion
        s_special = generate_random_string(length=100, include_digits=False, include_special=True)
        # Note: This test is probabilistic but highly likely to pass with length 100
        # Check if contains punctuation
        import string
        self.assertTrue(any(c in string.punctuation for c in s_special))

    def test_generate_random_number(self):
        val = generate_random_number(min_val=10, max_val=20)
        self.assertTrue(10 <= val <= 20)
        
        val_single = generate_random_number(min_val=5, max_val=5)
        self.assertEqual(val_single, 5)

    def test_generate_random_list(self):
        lst = generate_random_list(size=10, min_val=1, max_val=5)
        self.assertEqual(len(lst), 10)
        for val in lst:
            self.assertTrue(1 <= val <= 5)

    def test_shuffle_list(self):
        original = [1, 2, 3, 4, 5]
        shuffled = shuffle_list(original)
        self.assertEqual(len(shuffled), len(original))
        self.assertEqual(set(shuffled), set(original))
        self.assertNotEqual(id(original), id(shuffled)) # Should be a copy

    def test_random_choice(self):
        items = [1, 2, 3]
        choice = random_choice(items)
        self.assertIn(choice, items)
        
        self.assertIsNone(random_choice([]))

    def test_generate_random_float(self):
        val = generate_random_float(min_val=1.5, max_val=2.5)
        self.assertTrue(1.5 <= val <= 2.5)

    def test_generate_random_boolean(self):
        val = generate_random_boolean()
        self.assertIsInstance(val, bool)
        
        # Test probability boundaries (mocking random would be better but simple check here)
        with patch('random.random') as mock_random:
            mock_random.return_value = 0.1
            self.assertTrue(generate_random_boolean(probability=0.2))
            
            mock_random.return_value = 0.9
            self.assertFalse(generate_random_boolean(probability=0.2))

if __name__ == '__main__':
    unittest.main()
