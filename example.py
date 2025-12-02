"""
Example module with utility functions.
"""


def greet(name: str) -> str:
    """
    Greet a person by name.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}!"


def main():
    """Main function."""
    print(greet("World"))


if __name__ == "__main__":
    main()
