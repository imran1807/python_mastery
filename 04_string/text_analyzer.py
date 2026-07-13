def convert_to_uppercase(text):
    """
    Convert the input text to uppercase.

    Args:
        text (str): The input string to be converted.

    Returns:
        str: The uppercase version of the input string.
    """
    return text.upper()
def convert_to_lowercase(text):
    """
    Convert the input text to lowercase.

    Args:
        text (str): The input string to be converted.

    Returns:
        str: The lowercase version of the input string.
    """
    return text.lower()
def count_word(text, word):
    """
    Count the occurrences of a specific word in the input text.

    Args:
        text (str): The input string to search within.
        word (str): The word to count occurrences of.

    Returns:
        int: The number of occurrences of the specified word.
    """
    return text.count(word)
def count_character(text, character):
    """
    Count the occurrences of a specific character in the input text.

    Args:
        text (str): The input string to search within.
        character (str): The character to count occurrences of.

    Returns:
        int: The number of occurrences of the specified character.
    """
    return text.count(character)
def replace_word(text, old_word, new_word):
    """
    Replace occurrences of a specific word in the input text with a new word.

    Args:
        text (str): The input string to perform the replacement on.
        old_word (str): The word to be replaced.
        new_word (str): The word to replace with.

    Returns:
        str: The modified string with the specified word replaced.
    """
    return text.replace(old_word, new_word)
def reverse_text(text):
    """
    Reverse the input text.

    Args:
        text (str): The input string to be reversed.

    Returns:
        str: The reversed version of the input string.
    """
    return text[::-1]
if __name__ == "__main__":
    # Example usage of the functions
    sample_text = "Python is a programming language"
    print("Original Text:", sample_text)
    print("Uppercase:", convert_to_uppercase(sample_text))
    print("Lowercase:", convert_to_lowercase(sample_text))
    print("Count of 'a':", count_character(sample_text, 'a'))
    print("Count of 'programming':", count_word(sample_text, 'programming'))
    print("Replace 'Python' with 'Java':", replace_word(sample_text, 'Python', 'Java'))
    print("Reversed Text:", reverse_text(sample_text))