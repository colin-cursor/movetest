"""
Random utility functions for generating random data.
"""

import random
import string
from typing import List, Optional


def generate_random_string(length: int = 10, include_digits: bool = True, include_special: bool = False) -> str:
    """
    Generate a random string of specified length.
    
    Args:
        length: The length of the random string to generate
        include_digits: Whether to include digits in the string
        include_special: Whether to include special characters
    
    Returns:
        A random string of the specified length
    """
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))


def generate_random_number(min_val: int = 0, max_val: int = 100) -> int:
    """
    Generate a random integer between min_val and max_val (inclusive).
    
    Args:
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)
    
    Returns:
        A random integer in the specified range
    """
    return random.randint(min_val, max_val)


def generate_random_list(size: int = 5, min_val: int = 0, max_val: int = 100) -> List[int]:
    """
    Generate a list of random integers.
    
    Args:
        size: Number of elements in the list
        min_val: Minimum value for each element
        max_val: Maximum value for each element
    
    Returns:
        A list of random integers
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


def shuffle_list(items: List) -> List:
    """
    Return a shuffled copy of the input list.
    
    Args:
        items: The list to shuffle
    
    Returns:
        A new list with shuffled elements
    """
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled


def random_choice(items: List) -> Optional:
    """
    Return a random element from the list.
    
    Args:
        items: The list to choose from
    
    Returns:
        A random element from the list, or None if the list is empty
    """
    if not items:
        return None
    return random.choice(items)


def generate_random_float(min_val: float = 0.0, max_val: float = 1.0) -> float:
    """
    Generate a random float between min_val and max_val.
    
    Args:
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)
    
    Returns:
        A random float in the specified range
    """
    return random.uniform(min_val, max_val)


def generate_random_boolean(probability: float = 0.5) -> bool:
    """
    Generate a random boolean value.
    
    Args:
        probability: Probability of returning True (default: 0.5)
    
    Returns:
        A random boolean value
    """
    return random.random() < probability
