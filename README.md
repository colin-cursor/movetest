# init-utils

Small Python utility functions for generating random data and manipulating strings.

## Contents

- `init/random_utils.py`
  - `generate_random_string(length=10, include_digits=True, include_special=False)`
  - `generate_random_number(min_val=0, max_val=100)`
  - `generate_random_list(size=5, min_val=0, max_val=100)`
  - `shuffle_list(items)`
  - `random_choice(items)`
  - `generate_random_float(min_val=0.0, max_val=1.0)`
  - `generate_random_boolean(probability=0.5)`
- `init/string_utils.py`
  - `capitalize_words(text)`
  - `reverse_string(text)`
  - `truncate_string(text, max_length, suffix="...")`
  - `count_words(text)`
  - `remove_whitespace(text, preserve_single_space=False)`
  - `is_palindrome(text, case_sensitive=False)`
  - `snake_to_camel(text)`

## Requirements

- Python 3.8+ (uses standard library only)

## Usage

Run these examples from the repository root (`/workspace`):

```python
from init.random_utils import (
    generate_random_string,
    generate_random_number,
    generate_random_list,
)
from init.string_utils import (
    capitalize_words,
    truncate_string,
    is_palindrome,
)

print(generate_random_string(12, include_special=True))
print(generate_random_number(1, 6))
print(generate_random_list(size=3, min_val=10, max_val=20))

print(capitalize_words("hello world"))
print(truncate_string("abcdefghijklmnopqrstuvwxyz", max_length=10))
print(is_palindrome("A man a plan a canal Panama"))
```

## Notes

- This repo is intentionally minimal: no external dependencies and no packaging/publishing setup.
