import sys
import os
import unittest

# Add the parent directory to sys.path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from init.string_utils import (
    capitalize_words,
    reverse_string,
    truncate_string,
    count_words,
    remove_whitespace,
    is_palindrome,
    snake_to_camel
)

class TestStringUtils(unittest.TestCase):

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")
        self.assertEqual(capitalize_words(""), "")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("123"), "321")

    def test_truncate_string(self):
        self.assertEqual(truncate_string("hello world", 11), "hello world")
        self.assertEqual(truncate_string("hello world", 5), "he...")
        self.assertEqual(truncate_string("hello world", 8, suffix=".."), "hello ..")
        self.assertEqual(truncate_string("short", 10), "short")

    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words("  hello   world  "), 2)
        self.assertEqual(count_words(""), 0)

    def test_remove_whitespace(self):
        self.assertEqual(remove_whitespace("hello world"), "helloworld")
        self.assertEqual(remove_whitespace("hello world", preserve_single_space=True), "hello world")
        self.assertEqual(remove_whitespace("  hello   world  ", preserve_single_space=True), "hello world")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama")) # Case insensitive default + ignore spaces
        self.assertFalse(is_palindrome("hello"))
        
        self.assertFalse(is_palindrome("Racecar", case_sensitive=True))
        self.assertTrue(is_palindrome("RacecaR", case_sensitive=True))

    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")
        self.assertEqual(snake_to_camel("this_is_a_test"), "thisIsATest")
        self.assertEqual(snake_to_camel("simple"), "simple")

if __name__ == '__main__':
    unittest.main()
