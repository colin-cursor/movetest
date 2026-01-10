import random
import string

from init.random_utils import (
    generate_random_boolean,
    generate_random_float,
    generate_random_list,
    generate_random_number,
    generate_random_string,
    random_choice,
    shuffle_list,
)


def test_generate_random_string_length_and_charset_letters_only():
    random.seed(0)
    s = generate_random_string(length=32, include_digits=False, include_special=False)
    assert len(s) == 32
    assert all(ch in string.ascii_letters for ch in s)


def test_generate_random_string_can_include_digits_and_specials():
    random.seed(1)
    s = generate_random_string(length=128, include_digits=True, include_special=True)
    assert len(s) == 128
    allowed = set(string.ascii_letters + string.digits + string.punctuation)
    assert set(s).issubset(allowed)


def test_generate_random_number_in_range_inclusive():
    for _ in range(50):
        n = generate_random_number(min_val=5, max_val=7)
        assert 5 <= n <= 7


def test_generate_random_list_size_and_range():
    xs = generate_random_list(size=20, min_val=-2, max_val=2)
    assert len(xs) == 20
    assert all(-2 <= x <= 2 for x in xs)


def test_shuffle_list_returns_new_list_with_same_elements():
    random.seed(0)
    items = [1, 2, 3, 4, 5]
    shuffled = shuffle_list(items)
    assert shuffled is not items
    assert sorted(shuffled) == sorted(items)


def test_random_choice_empty_is_none():
    assert random_choice([]) is None


def test_random_choice_singleton():
    assert random_choice(["x"]) == "x"


def test_generate_random_float_in_range():
    for _ in range(50):
        x = generate_random_float(min_val=1.5, max_val=2.5)
        assert 1.5 <= x <= 2.5


def test_generate_random_boolean_probability_extremes():
    # Deterministic at extremes, regardless of random state.
    for _ in range(50):
        assert generate_random_boolean(probability=0.0) is False
        assert generate_random_boolean(probability=1.0) is True

