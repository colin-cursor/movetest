# Python Utilities

A collection of Python utility functions for common operations.

## Modules

### `init/random_utils.py`

Random utility functions for generating random data:

- `generate_random_string(length, include_digits, include_special)` - Generate a random string
- `generate_random_number(min_val, max_val)` - Generate a random integer
- `generate_random_list(size, min_val, max_val)` - Generate a list of random integers
- `shuffle_list(items)` - Return a shuffled copy of a list
- `random_choice(items)` - Return a random element from a list
- `generate_random_float(min_val, max_val)` - Generate a random float
- `generate_random_boolean(probability)` - Generate a random boolean

### `init/string_utils.py`

String utility functions for text manipulation:

- `capitalize_words(text)` - Capitalize the first letter of each word
- `reverse_string(text)` - Reverse a string
- `truncate_string(text, max_length, suffix)` - Truncate a string with suffix
- `count_words(text)` - Count words in text
- `remove_whitespace(text, preserve_single_space)` - Remove extra whitespace
- `is_palindrome(text, case_sensitive)` - Check if a string is a palindrome
- `snake_to_camel(text)` - Convert snake_case to camelCase

## Usage

```python
from init.random_utils import generate_random_string, generate_random_number
from init.string_utils import capitalize_words, is_palindrome

# Generate a random string
random_str = generate_random_string(length=15, include_digits=True)

# Generate a random number
random_num = generate_random_number(1, 100)

# Capitalize words
text = capitalize_words("hello world")  # "Hello World"

# Check palindrome
result = is_palindrome("A man a plan a canal Panama")  # True
```

## Requirements

- Python 3.x
