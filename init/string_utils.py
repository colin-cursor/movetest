"""
String utility functions for text manipulation and formatting.
"""

from typing import List, Optional


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in the text.
    
    Args:
        text: The input text to capitalize
    
    Returns:
        Text with each word capitalized
    """
    return ' '.join(word.capitalize() for word in text.split())


def reverse_string(text: str) -> str:
    """
    Reverse the input string.
    
    Args:
        text: The string to reverse
    
    Returns:
        The reversed string
    """
    return text[::-1]


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length and add a suffix.
    
    Args:
        text: The string to truncate
        max_length: Maximum length of the resulting string (including suffix)
        suffix: String to append when truncated (default: "...")
    
    Returns:
        The truncated string with suffix if applicable
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix


def count_words(text: str) -> int:
    """
    Count the number of words in the text.
    
    Args:
        text: The text to count words in
    
    Returns:
        The number of words
    """
    return len(text.split())


def remove_whitespace(text: str, preserve_single_space: bool = False) -> str:
    """
    Remove extra whitespace from text.
    
    Args:
        text: The text to clean
        preserve_single_space: If True, preserves single spaces between words
    
    Returns:
        Text with whitespace removed or normalized
    """
    if preserve_single_space:
        return ' '.join(text.split())
    return ''.join(text.split())
