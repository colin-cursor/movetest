from init.string_utils import (
    capitalize_words,
    count_words,
    is_palindrome,
    remove_whitespace,
    reverse_string,
    snake_to_camel,
    truncate_string,
)


def test_capitalize_words_collapses_whitespace():
    assert capitalize_words(" hello   world ") == "Hello World"


def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""


def test_truncate_string_no_truncation_when_short_enough():
    assert truncate_string("hello", max_length=5) == "hello"
    assert truncate_string("hello", max_length=10) == "hello"


def test_truncate_string_truncates_and_includes_suffix():
    assert truncate_string("hello world", max_length=8, suffix="...") == "hello..."
    assert truncate_string("hello world", max_length=8, suffix="..") == "hello .."


def test_truncate_string_handles_small_max_length():
    assert truncate_string("hello", max_length=0) == ""
    assert truncate_string("hello", max_length=2) == ".."
    assert truncate_string("hello", max_length=3) == "..."


def test_count_words_splits_on_whitespace():
    assert count_words("a b  c") == 3
    assert count_words("") == 0


def test_remove_whitespace_modes():
    assert remove_whitespace(" a  b\tc\n") == "abc"
    assert remove_whitespace(" a  b\tc\n", preserve_single_space=True) == "a b c"


def test_is_palindrome_ignores_non_alnum_and_case_by_default():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("Hello, world") is False


def test_is_palindrome_case_sensitive_option():
    assert is_palindrome("Aa", case_sensitive=False) is True
    assert is_palindrome("Aa", case_sensitive=True) is False


def test_snake_to_camel_basic_and_edge_cases():
    assert snake_to_camel("snake_case") == "snakeCase"
    assert snake_to_camel("") == ""
    assert snake_to_camel("_leading") == "Leading"

